import guilherme, felipe

x = int (input("Insira o valor de X: "))
y = int (input("Insira o valor de Y: "))

escolha = int(input("Escolha a operação que deseja fazer:\n1 - Soma. 2 - Subtração 3 - Multiplicação. 4 - Divisão.\n"))

if escolha == 1:
    print("O resultado da soma é", guilherme.soma(x, y))
elif escolha == 2:
    print("O resultado da subtração é", guilherme.subtracao(x, y))
elif escolha == 3:
    print('A multiplicação dos números escolhidos é:',felipe.multiplicacao(x,y))
elif escolha == 4:
    print('A divisão dos números escolhidos é:',felipe.divisao(x,y))