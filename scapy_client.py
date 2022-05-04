from scapy.all import *
from scapy.utils import rdpcap
import time
from text_to_bit_codder import text_from_bits, text_to_bits

pkts = rdpcap("packets/RDPUDP_3.pcap")

thisdict = {
    "00" : pkts[0], # IP.id = 36287 
    "01" : pkts[1], # 36338
    "10" : pkts[2], # 36348
    "11" : pkts[3], # 36502
}

antygona = ""
with open("Sofokles-Antygona.txt",encoding="ANSI") as f:
    for line in f:
        antygona += line # size 51720 

bits = text_to_bits(antygona[:30000]) 
n = 2
chunks = [bits[i:i+n] for i in range(0, len(bits), n)]
for chunk in chunks:
    sendp(thisdict[chunk])
    time.sleep(0.001)
