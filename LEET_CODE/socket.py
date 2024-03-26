import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('localhost', 5000)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a client to connect
    print('waiting for a connection')
    client_sock, client_address = sock.accept()

    try:
        # Receive data from the client
        print('received data:', client_address)
        data = client_sock.recv(16)

        # Send data back to the client
        if data:
            print('sent data:', repr(data))
            client_sock.sendall(data)
        else:
            print('no data from', client_address)
    finally:
        # Clean up the connection
        client_sock.close()


import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the server
server_address = ('localhost', 5000)
sock.connect(server_address)

# Send data to the server
message = 'Hello, server!'
sock.sendall(message.encode())

# Receive data from the server
received = sock.recv(16)

# Print the received data
print('received message:', repr(received.decode()))

# Clean up the connection
sock.close()      