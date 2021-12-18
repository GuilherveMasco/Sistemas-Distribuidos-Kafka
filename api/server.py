import socket
import tweepy
from kafka import KafkaProducer
from kafka import KafkaConsumer
from kafka import KafkaAdminClient
import kafka

tweeter_bearer_token = "AAAAAAAAAAAAAAAAAAAAAOxzWwEAAAAAuAPkErXtqs9SmUGlYwXgvEpJFq8%3DM2VUJiUD8AVP1qibga3ueWh3B70wChGbU3jIUBGekdWd7PyVme"

def read_topic(topic_name, client_sock):
	consumer = KafkaConsumer(("topic_" + topic_name), bootstrap_servers=["localhost:9092"], auto_offset_reset="earliest", enable_auto_commit=True)
	
	return consumer
		
def tweeter_reader(keyword, topic_name):
	client = tweepy.Client(bearer_token=tweeter_bearer_token)
	query = keyword + " -is:retweet"
	tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'], user_fields=['profile_image_url'], expansions='author_id', max_results=10)
	
	producer = KafkaProducer(bootstrap_servers='localhost:9092')
	counter = 0
	if (tweets):
		for tweet in tweets.data:
			counter = counter + 1
			text = "\n" + str(counter) + " ------------\n" + str(tweet)
			producer.send(topic_name, text.encode())

def topic_create(name, partitions):
	kafka_admin = KafkaAdminClient(bootstrap_servers="localhost:9092")
	new_topic = kafka.admin.NewTopic(name=("topic_" + name), num_partitions=partitions, replication_factor=1)
	response = kafka_admin.create_topics([new_topic])
	
	if (response.topic_errors[0][2] == None):
		tweeter_reader(name, ("topic_" + name))
		return "Status: Sucesso"
	else:
		return "Erro: " + response.topic_errors[0][2]

def topic_delete(name):
	kafka_admin = KafkaAdminClient(bootstrap_servers="localhost:9092")
	response = kafka_admin.delete_topics(["topic_" + name])

	if (response.topic_error_codes[0][1] == 0):
		return "Status: Sucesso"
	else:
		return "Erro: topico nao existe"

def server():
	# Create server socket.
	serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)

	# Bind server socket to loopback network interface.
	serv_sock.bind(('127.0.0.1', 6543))

	# Turn server socket into listening mode.
	serv_sock.listen(10)

	while True:
		  # Accept new connections in an infinite loop.
		  client_sock, client_addr = serv_sock.accept()
		  print('New connection from', client_addr)

		  chunks = []
		  while True:
		      # Keep reading while the client is writing.
		      data = client_sock.recv(2048)
		      if not data:
		          # Client is done with sending.
		          break
		      chunks.append(data)
		  request = chunks[0].decode("UTF-8")
		  params = request.split(' ')

		  role = params[0]
		  action = params[1]
		  topic_name = params[2]

		  if (role == "manager"):
		    print("--> [MANAGER] " + request)
		    
		    response = ""
		    if (action == "create_topic"):
		    	partitions = int(params[3])
		    	response = topic_create(topic_name, partitions)
		    elif (action == "delete_topic"):
		    	response = topic_delete(topic_name)
		    else:
		    	responde = "Erro: Ação inválida."
		    print("--> " + response)
		    
		    client_sock.sendall(response.encode())
		    client_sock.close()
		  elif (role == "client"):
		    print("--> [CLIENT] " + request)
		    consumer = read_topic(topic_name, client_sock)
		    
		    counter = 1
		    for message in consumer:
		    	if (counter == 10):
		    		break
		    	# print(message.value.decode("utf-8") + "\n=================\n")
		    	client_sock.sendall(message.value)
		    	counter = counter + 1
		    	
		    client_sock.close()
		  else:
		    print("Error: invalid role")
		    client_sock.sendall('ERRO: seu serviço não tem permissão para executar'.encode())
		    client_sock.close()

server()
