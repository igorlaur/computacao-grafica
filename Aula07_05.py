
def funcao():
    global teste # muda o escopo de teste

    teste = 1  # escopo globa
    print('Funcao:', teste)

teste = 0  # escopo global 

funcao()

print('Global:', teste)
