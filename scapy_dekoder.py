from socket import timeout
from scapy.all import *
from text_to_bit_codder import text_from_bits, text_to_bits
#ip.id == 36287 or ip.id == 36338 
captures = sniff(timeout=600, filter="dst 192.168.1.14 and udp")

bits = ''

resolve_dict = {
    36287 :"00", 
    36338: "01",
    36348: "10",
    36502: "11"
}

for cap in captures:
    if cap[IP].id in resolve_dict:
        bits += resolve_dict[cap[IP].id]
print(bits)
print(text_from_bits(bits))
 # wrpcap('Captured_1.pcap', captures)