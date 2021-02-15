C = {'a':10, 'b':1, 'c':22}
tmp = list()
for k,v in C.items():
    '''
    lista de valores que e estavam
    no dicionario
    '''
    tmp.append((v,k))
for c,v in tmp:
    print(c)

print(type(tmp))
tmp = sorted(tmp,reverse=True)
print(tmp)

