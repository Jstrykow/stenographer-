antygona = ""
with open("antygona.txt",encoding="utf8") as f:
    for line in f:
        antygona += line

byte_antygona = bytes(antygona, 'utf-8')
print(byte_antygona)

# dobra to akcja jest taka, że na dwóch bajtach zapisywana jest utf-8 i musimy dwa baity przerzicać dla jednego znaku