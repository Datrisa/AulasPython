# **** tentativa e acertos de um numero.

nome = input('Qual seu Nome? \n')
print(f'{nome}, Agradecemos sua Participação!!')
print(f'    {nome}, Tente acertar o número secreto')
numero = 12
tentativas = 3
rodadas = 1
while(rodadas <= tentativas):
    print(f'    Tentativa {rodadas} de {tentativas} tentativas')
    chute=int(input('Digite um numero menor que 20:'))
    print(f'{nome}, você digitou {chute}')
    acertou = chute == numero
    maior = chute > numero
    menor = chute < numero

    if(acertou):
        print('     Parabéns, Você acertou.\n')
        break
    elif(maior):
        print('     Ooopsss, deu ruim, este número é maior\n')
    elif(menor):
        print('     Hhummm, este número é menor\n')
    rodadas = rodadas + 1
    #tentativas = tentativas - 1
input(f'{nome}, digite ENTER para sair.')