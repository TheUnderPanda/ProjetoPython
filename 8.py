def salario(x,y):
    Q_salario = float(x)
    horas = float(y)
    return Q_salario*horas
NUMBER = input()
H_Trabalho = input()
H_Salario = input()
print("NUMBER =",NUMBER)
print("SALARY = U$ %.2f" % salario(H_Trabalho,H_Salario))
