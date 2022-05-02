from scapy.all import *
from scapy.utils import rdpcap
import time
from text_to_bit_codder import text_from_bits, text_to_bits
 
from text_to_bit_codder import text_to_bits
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
    "11" : pkts[3],
}

# chosen random packets 
"""
print(pkts[0][IP].id)
print(pkts[1][IP].id)
print(pkts[2][IP].id)
print(pkts[3][IP].id)
"""


antygona = ""
with open("Sofokles-Antygona.txt",encoding="ANSI") as f:
    for line in f:
        antygona += line

bits = text_to_bits(antygona[8000:9000])
n = 2
chunks = [bits[i:i+n] for i in range(0, len(bits), n)]
for chunk in chunks:
    sendp(thisdict[chunk])
    time.sleep(0.001)
# print(shorter_bits)
