from scapy.all import *
from scapy.utils import rdpcap
from random import randint

for i in range(7):
    # dupa = 5  + randint(0, 5)
    # print(dupa)
    clean_sniff = sniff(timeout = (200 + randint(0, 300)) )# 180 100
    wrpcap(f"dist/pcap_clean_{i + 1}.pcap", clean_sniff)

