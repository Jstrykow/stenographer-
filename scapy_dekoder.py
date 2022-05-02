from itertools import count
from socket import timeout
from scapy.all import *
from text_to_bit_codder import text_from_bits, text_to_bits
#ip.id == 36287 or ip.id == 36338 
captures = sniff(count=20000) #filter="dst 192.168.1.14 and udp")

bits = ''
resolve_text = ""

resolve_dict = {
    36287:"00", 
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
                resolve_text += str(text_from_bits(chunk))
                chunk = ""
print(resolve_text)

with open("received_antygona_2.txt", "w", encoding="ANSI") as f:
    f.write(bits)

with open("received_antygona_2_decoded.txt", "w", encoding="ANSI") as f:
    try:
        f.write(resolve_text)
    except e:
        pass

wrpcap('Captured_host_3.pcap', captures)
