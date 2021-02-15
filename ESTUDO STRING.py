#STRING REVERSO
'''
fruta = "banana"
ancora = 0
tamanho = len(fruta)
while ancora < len(fruta):
    tamanho -= 1
    print(fruta[tamanho])
    ancora += 1
'''


'''
#FIND - ENCONTRA POSIÇÃO RELATIVA A STRING
palavra = "ygor"
print(palavra.find("y"))

'''


text = 'X-DSPAM-Confidence:0.8475'
anco = text.find(":")
text=text[anco+1:]
text = float(text)
print(text)

