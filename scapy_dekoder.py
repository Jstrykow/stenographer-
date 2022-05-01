from socket import timeout
from scapy.all import *
from text_to_bit_codder import text_from_bits, text_to_bits
#ip.id == 36287 or ip.id == 36338 
captures = sniff(timeout=500,filter="dst 192.168.1.14 and udp")

bits = ''

for cap in captures:
    # print(cap[IP].id)
    # print(type(cap[IP].id))
    if cap[IP].id == 36287:
        bits += '0'
    elif cap[IP].id == 36338:
        bits += '1'
print(bits)
print(text_from_bits(bits))

wrpcap('sniffed.pcap', captures)