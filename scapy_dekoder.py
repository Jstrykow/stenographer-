from socket import timeout
from scapy.all import *
from text_to_bit_codder import text_from_bits, text_to_bits
#ip.id == 36287 or ip.id == 36338 
captures = sniff(timeout=100) #filter="dst 192.168.1.14 and udp")

bits = ''
resolve_text = ""

resolve_dict = {
    36287 :"00", 
    36338: "01",
    36348: "10",
    36502: "11"
}
chunk = ""
for cap in captures:
    if cap.haslayer(IP):
        if cap[IP].id in resolve_dict:
            bits += resolve_dict[cap[IP].id]
            chunk += resolve_dict[cap[IP].id]
            if len(chunk) == 8:
                resolve_text += text_from_bits(chunk)
                chunk = ""
print(resolve_text)
wrpcap('Captured_1.pcap', captures)