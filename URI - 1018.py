A = int(input())

#DiVISÃO POR 100
valor = [100,50,20,10,5,2,1]
notas = [(100)]
for x in valor:
    print("%.i nota(s) de R$ " % (A/x))
    if (A%x < 0):
        print("0 nota(s) de R$ 100,00")

'''
print("%.i nota(s) de R$ 100,00" % (A/100))
A = A%100
if A < 0:
        print("0 nota(s) de R$ 100,00")
#////////////////////////////////////////////
#DIVISÃO POR 50

print("%.i nota(s) de R$ 50,00" % (A/50))
A = A%50
if A < 0:
        print("0 nota(s) de R$ 50,00")
#////////////////////////////////////////////////
#DIVISÃO POR 20
print("%.i nota(s) de R$ 20,00" % (A/20))
A = A%20
if A < 0:
        print("0 nota(s) de R$ 20,00")

#////////////////////////////////////////////////
#DIVISÃO POR 10
print("%.i nota(s) de R$ 10,00" % (A/10))
A = A%10
if A < 0:
        print("0 nota(s) de R$ 10,00")

#////////////////////////////////////////////////
#DIVISÃO POR 5
print("%.i nota(s) de R$ 5,00" % (A/5))
A = A%5
if A < 0:
        print("0 nota(s) de R$ 5,00")

#////////////////////////////////////////////////
#DIVISÃO POR 2
print("%.i nota(s) de R$ 2,00" % (A/2))
A = A%2
if A < 0:
        print("0 nota(s) de R$ 2,00")

#////////////////////////////////////////////////
#DIVISÃO POR 1
print("%.i nota(s) de R$ 1,00" % (A/1))
A = A%1
if A < 0:
#        print("0 nota(s) de R$ 1,00")
'''