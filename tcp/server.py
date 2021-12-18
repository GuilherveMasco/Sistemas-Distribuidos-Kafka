import socket

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
    partitions = params[3]

    if (role == "manager"):
      print("--> [MANAGER] " + request)
      client_sock.sendall(b''.join(chunks))
      client_sock.close()
    elif (role == "client"):
      print("--> [CLIENT] " + request)
      client_sock.sendall(b''.join(chunks))
      client_sock.close()
    else:
      print("Error: invalid role")
      client_sock.sendall('ERRO: seu serviço não tem permissão para executar'.encode())
      client_sock.close()
    
