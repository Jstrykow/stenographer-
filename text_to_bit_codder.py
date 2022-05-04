
"""
antygona = ""
with open("Sofokles-Antygona.txt",encoding="ANSI") as f:
    for line in f:
        antygona += line
"""
# https://stackoverflow.com/questions/7396849/convert-binary-to-ascii-and-vice-versa
def text_to_bits(text, encoding='ANSI', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def text_from_bits(bits, encoding='ANSI', errors='ignore'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

"""
print(len(antygona))
bits = text_to_bits(antygona)
print(len(bits))
text = text_from_bits(bits)

with open("test.txt", "w", encoding="ANSI" ) as f:
    f.write(text)

n = 2
chunks = [bits[i:i+n] for i in range(0, len(bits), n)]
for i in range(0,len(chunks),4):
    chunk = chunks[i] + chunks[i+1] +  chunks[i+2] + chunks[i+3]
    print(chunk)
    print(text_from_bits(chunk))



#    print(len(text_to_bits(i)))
#    print(i)
# print(bits)
"""