
def funcao():
    teste = 1  # escopo interno da funcao
    print('Funcao:', teste)

teste = 0  # escopo global 

funcao()

print('Global:', teste)
