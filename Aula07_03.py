
def funcao_menor (*x):
   if x:  # verifica se existe ao menos um elemento.
        menor = x[0]
        for valor in x[1:]:
            if valor < menor:
                menor = valor
        print(menor)


print("------funcao_menor(1)")
funcao_menor(1)
print("-------")

print("------funcao_menor(1,5)")
funcao_menor(1,5)
print("-------")

print("------funcao_menor(1,5,3)")
funcao_menor(1,5,3,0)
print("-------")

