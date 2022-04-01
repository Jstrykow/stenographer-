import socket

target_host = "127.0.0.1"
target_port = 9998

# making an socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connection with server
client.connect((target_host, target_port))


text = "óżąść"
text = text * 256
print(text)
# send of data
data = text
client.send(data.encode())

# respond of data
response = client.recv(4096)

print(response.decode())
client.close()