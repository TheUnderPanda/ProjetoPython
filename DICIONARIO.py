abri = input("digite o nome do arquivo")

try:
    op = open(abri)
except:
    quit()
i = 0
Dicn = dict()
for x in op:
    x = x.split()
    for y in range(len(x)):
        Str = x[y]
        print(Str)
        Dicn[Str] = i
        i += 1

print(Dicn)
