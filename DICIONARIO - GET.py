nome = ['ygor','ygor', 'paulo','olinda']
Dic = dict()

for x in nome:
    Dic[x] = Dic.get(x, 0) + 1
print(Dic)
