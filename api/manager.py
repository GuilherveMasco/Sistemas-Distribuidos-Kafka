import sys
import socket

def manager():
  args = sys.argv
  action = args[1]
  topic_name = args[2]
  partitions = '1'
  if (action == "create_topic" and len(args) > 3):
    partitions = args[3]

  request = 'manager '
  if (action == "create_topic"):
    request = request + action + ' ' + topic_name + ' ' + partitions
  elif (action == "delete_topic"):
    request = request + action + ' ' + topic_name
  else:
    print("Erro: Ação inválida. Escolha as ações create_topic ou delete_topic.")
    return -1

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
      
  print((b''.join(chunks)).decode("UTF-8"))

  # Disconnect from server.
  client_sock.close()

manager()
