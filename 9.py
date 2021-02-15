def comissao(x,z):
    N_comissao = float(x)
    N_venda = float(z)

    return N_venda*N_comissao

Nome_vendedor = input()
Salario = float(input())
venda = input()
Ncomissao = 0.15
#COMISSÃO 15%
Novo_Salario  = Salario + comissao(Ncomissao,venda)

print("TOTAL = U$ %.2f" % Novo_Salario)

