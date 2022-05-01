from scapy.all import *
from scapy.utils import rdpcap
import time
from text_to_bit_codder import text_from_bits, text_to_bits
"""
0 36287 0
1 36338 1
2 36348 10
3 36502 11
4 36503 100
5 36506 101
6 36565 
7 36569 
8 36572 
9 36731 
10 36734 
11 36775 
12 36784 
13 36793 
14 36800 
15 37032 
"""

pkts = rdpcap("RDPUDP_3.pcap")

thisdict = {
    "00" : pkts[0], 
    "01" : pkts[1],
    "10" : pkts[2],
    "11" : pkts[3]
}

# chosen random packets 
pkts = rdpcap("RDPUDP_3.pcap")

# print(type(pkts[0][IP].id))
# pkts[1].show()


from text_to_bit_codder import text_to_bits

antygona = ""
with open("antygona.txt",encoding="utf8") as f:
    for line in f:
        antygona += line

bits = text_to_bits(antygona) # 443032
# print(len(bits))
shorter_bits = bits[0:1000]

for bit in shorter_bits:
    if bit == '0':
        #print()
        # pkt = thisdict["0"]
        # print(thisdict["0"][IP].id)
        sendp(thisdict["0"])
    elif bit == '1':
        sendp(thisdict["1"])
        # print(thisdict["1"][IP].id)
    time.sleep(0.001)
print(shorter_bits)
print(text_from_bits(shorter_bits))