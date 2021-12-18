import sys
import socket

def client():
  args = sys.argv
  action = args[1]
  topic_name = args[2]
  partition = '1'
  if (action == "subscribe_topic"):
    if (len(args) > 3):
      partition = args[3]
  else:
    print("Erro: Ação inválida. Utilize a ação subscribe_topic.")
    return -1

  request = "client " + action + ' ' + topic_name + ' ' + partition


  # Create client socket.
  client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  # Connect to server (replace 127.0.0.1 with the real server IP).
  client_sock.connect(("127.0.0.1", 6543))
  # Send some data to server.
  client_sock.sendall(request.encode())
  client_sock.shutdown(socket.SHUT_WR)

  # Receive some data back.
  chunks = []
  while True:
  		data = client_sock.recv(2048)
  		if not data:
  			break
  		chunks.append(data)
  		print(data.decode("UTF-8"))
  print(repr(b''.join(chunks)))

  # Disconnect from server.
  client_sock.close()

client()
