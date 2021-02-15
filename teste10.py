arquivo = input("digite o nome do arquivo")
try:
    abri = open(arquivo)
except:
    print("Arquivo não encontrado")
    quit()

Dic = dict()
for x in abri:
    x.split()
    if x.startswith("From "):
        item = x[-14:-12]
        Dic[item] = Dic.get(item,0)+1



Dic = sorted(Dic.items())
for k,v in Dic:
    print(k,v)