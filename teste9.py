nome = input("DIGITE O NOME DO ARQUIVO")
try:
    dado = open(nome)
except:
    quit()
lista = list()
maior = 0
Dicionario = dict()
for linha in dado:
        linha.split()
        if linha.startswith("From:")==True:
            comeco = linha.index(":")
            E_mail = linha[comeco+1:]
            if E_mail not in Dicionario:
                Dicionario[E_mail]= 1
            else:
                Dicionario[E_mail] = Dicionario[E_mail]+1
chave = str
maior = 0
op = 0
for key,val in Dicionario.items():
    if val > maior:
        maior = val
        chave = key


print("{} {}".format(chave.strip(),maior))




