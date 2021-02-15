fname = input("digite o nome do arqruivo")
fh = open(fname)
count = 0

for x in fh:
    if x.startswith("From:"):
        count += 1
        x = x.split()
        print(x[1])

print("There were", count, "lines in the file with From as the first word")

    #linha = linha.split()
    #lista = lista.append(linha)

'''
    linha = linha.split()
    lista.append(linha)
    lista.sort()
    print(lista)
'''

'''p_phrase = "was it a car or a cat I saw"


for x in range(len(p_phrase)):
     r_phrase = p_phrase[::-1]

'''

#stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
#org = "The organization for health, safety, and education"
#org = org.split(" ")
#acro = [ ]
#for x in org:
#    for y in stopwords:
#        if x == y:
#            org.remove(x)
#
#for z in org:
#    print(z)
#    ops= z[0]
#    p = z[-1]
#    if p == ",":
#        z = z[-2]
#        ops = ops + z
#        ops.upper()
#        acro.append(ops)
#    else:
#        ops = ops + z[-1]
#        ops.upper()
#        acro.append(ops)

#print(acro)



#scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"
#scores = scores.split(" ")
#ponteiro = 0
#for x in scores:
#    x = int(x)
#    if x >= 90:
#        ponteiro += 1
#print(ponteiro)
#---------------------------------------------------------------------------------------------------------------#


#wrds = ["end", 'work', "play", "start", "walk", "look", "open", "rain", "learn", "clean"]
#past_wrds = []
#for x in wrds:
#    x = x + "ed"
#    past_wrds.append(x)
#print(past_wrds)
#-------------------------------------------------------------------------------------------------------#
#output = " "
#t= 0
#for x in range(35):
#    t = x+1
#    output = output + "a"
#print(t)

#----------------------------------------------------------------------------------------------------------#

#str1 = "I love python"
#chars = [ ]
#for x in str1:
#    chars.append(x)
#print(chars)