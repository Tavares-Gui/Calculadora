import felipe

x = int(input('Insira o valor de X: '))
y = int(input('Insira o valor de Y: '))

escolha = int(input('Qual operação você deseja realizar?\n3- Multiplicação. 4- Divisão.'))

if escolha == 3:
    print('A multiplicação dos números escolhidos é:',felipe.multiplicacao(x,y))
elif escolha == 4:
    print('A divisão dos números escolhidos é:',felipe.divisao(x,y))
