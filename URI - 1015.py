import math
def retorno(x1,y1,x2,y2):
    x1 = float(x1)
    x2 = float(x2)
    y1 = float(y1)
    y2 = float(y2)

    X = pow((x2 - x1),2)
    Y = pow((y1 - y2),2)

    return math.sqrt(X+Y)

x1,y1 = input().split(" ")
x2,y2 = input().split(" ")

print("%.4f" % retorno(x1,y1,x2,y2))