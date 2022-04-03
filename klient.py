import socket
from text_to_bit_codder import text_to_bits, text_from_bits

antygona = ""
with open("antygona.txt",encoding="utf8") as f:
    for line in f:
        antygona += line

# bits = text_to_bits(antygona)
#bits = bits[0:100]
bits = '01'

target_host = "127.0.0.1"
target_port = 9998


for b in bits:
    # making an socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.connect((target_host, target_port))


    # send of data
    data = " "
    if b == '0':
        # data = "0"
        client.send(data.encode())
        client.send(data.encode())
        client.send(data.encode())
        print("0 sent")
    elif b == '1':
        # data = "1"
        client.send(data.encode())
        client.send(data.encode())
        client.send(data.encode())
        client.send(data.encode())
        client.send(data.encode())
        client.send(data.encode())
        print("1 sent")
    
    print(f"{b} {data}")
    # respond of data
    response = client.recv(4096)

    print(response.decode())
    client.close()
 
