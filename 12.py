def triangulo(x,y):
    return (x*y)/2
def circulo(C):
    A = 3.14159*pow(C,2)
    return A
def trapezio(x,y,z):
    A = (x+y)*z/2
    return A
def quadrado(x):
    return x*x
def retangulo(y,x):
    return y*x

A, B, C = input().split(" ")
A = float(A)
B = float(B)
C = float(C)
print("TRIANGULO: %.3f" % (triangulo(A,C)))
print("CIRCULO: %.3f" % (circulo(C)))
print("TRAPEZIO: %.3f" % (trapezio(A,B,C)))
print("QUADRADO: %.3f" % (quadrado(B)))
print("RETANGULO: %.3f" % (retangulo(A,B)))