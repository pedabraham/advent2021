cuenta = []

def register(number,cuenta):
    i = 0
    for bit in number:
        bit = int(bit)
        cuenta[i][bit] += 1
        i += 1

final_n = []
mask = []
# imit final_n



with open('input3') as input3:
    line = input3.readline()
    line = line.strip()
    lineSize = len(line)
    for i in range(lineSize):
        cuenta.append({1:0,0:0})
        final_n.append(0)
        mask.append(1)
    print(cuenta)
    register(line,cuenta)
    while True:
        line = input3.readline()
        line = line.strip()
        register(line,cuenta)
        if not line:
            break

i = 0
for bit in cuenta:
    if bit[1] > bit[0]:
        final_n[i] = 1
    else:
        final_n[i] = 0
    i += 1

def intcaststr(bitlist):
    return int("".join(str(i) for i in bitlist), 2)
mask = intcaststr(mask)
print(cuenta)
print(final_n)
print(intcaststr(final_n))
gamma = intcaststr(final_n)
epsilon = mask ^ gamma
print(epsilon)
print(epsilon*gamma)
