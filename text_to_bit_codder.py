

antygona = ""
with open("Sofokles-Antygona.txt",encoding="ANSI") as f:
    for line in f:
        antygona += line

# https://stackoverflow.com/questions/7396849/convert-binary-to-ascii-and-vice-versa
def text_to_bits(text, encoding='ANSI', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def text_from_bits(bits, encoding='ANSI', errors='ignore'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

for i in antygona[10:1000]:
    print(len(text_to_bits(i)))
    print(i)
# print(bits)
# print(text_from_bits(bits))
