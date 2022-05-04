from scapy.all import IP 
from scapy.utils import rdpcap
# from scapy.all.IP import * 
from scapy.packet import *
from text_to_bit_codder import text_from_bits, text_to_bits
import sys
# from PyInstaller.utils.hooks import collect_submodules
#ip.id == 36287 or ip.id == 36338 

# hiddenimports = collect_submodules('scapy.layers')

resolve_dict = {
    36287: "00", 
    36338: "01",
    36348: "10",
    36502: "11"
}

def read_antygona_from_pcap(file_name):
    # "/Users/Administrator/Documents/aaStudia/BEST\pcaps/pcap_contaminated_1.pcap"
    captures = rdpcap(f"{file_name}")
    bits = ''
    resolve_text = ""
    chunk = ""
    for cap in captures:
        if cap.haslayer(IP):
            if cap[IP].id in resolve_dict:
                bits += resolve_dict[cap[IP].id]
                chunk += resolve_dict[cap[IP].id]
                if len(chunk) == 8:
                    resolve_text += str(text_from_bits(chunk))
                    chunk = ""
                    print("CALCULATE")
    print(resolve_text)

    with open(f"received_antygona_binary.txt", "w", encoding="ANSI") as f:
        f.write(bits)

    with open(f"received_antygona_resolve_text.txt", "w", encoding="ANSI") as f:
        try:
            f.write(resolve_text)
        except:
            pass


def main():
    print("ROZPOCZE")
    read_antygona_from_pcap(sys.argv[1])

if __name__ == '__main__':
    main()