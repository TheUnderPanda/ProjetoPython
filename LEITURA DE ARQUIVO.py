fname = input("Enter file name: ")
fh = open(fname)
x = "X-DSPAM-Confidence:"
soma = 0
M_numero = 0
for line in fh:
   if not line.startswith(x):
      continue
   else:
      M_numero += 1
      dec = line.index(":")
      numero = float(line[dec+1:])
      soma = soma+numero

media = soma/M_numero
print(media)


'''
arquivo = input("difite o nome do arquivo \n")
#p = t.read()
try:
   t = open(arquivo)
except:
   print("Erro arquivo não encontrado")
   quit()

for line in t:
   if line.startswith('From:'):
      print(line)
'''


      # TIRA OS ESPAÇOS E BRANCO da direita
      #line = line.rstrip()

      #hy = line.index('@')
      #space = line.index(" ")
      #print(line[space:hy])



'''
ancoro = 0
for x in t:
   ancoro +=1
print(ancoro)
'''