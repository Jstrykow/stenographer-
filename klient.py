import socket
from text_to_bit_codder import text_to_bits, text_from_bits

antygona = ""
with open("antygona.txt",encoding="utf8") as f:
    for line in f:
        antygona += line

# bits = text_to_bits(antygona)
#bits = bits[0:100]
bits = '010101010101011111000'

target_host = "127.0.0.1"
target_port = 9998
# 49152-65535

"""
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
DESTINATION_ADDR = '127.0.0.1'
SOURCE_PORT, DESTINATION_PORT = 49153, 9998
sock.bind(('127.0.0.1', SOURCE_PORT))
sock.connect((DESTINATION_ADDR, DESTINATION_PORT))
sock.close()

"""
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.bind(("127.0.0.1", 51001))
client.connect((target_host, target_port))

# response = client.recv(4096)

# print(response.decode())
client.close()
