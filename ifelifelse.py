#  **** IF ELIF ELSE

# **** MODO 01 para apresentar comparação e acerto)

numero = int(50)
chute = int(input('digite um numero sem virgula: \n'))

if chute == numero:
    print('aaaa Você acertouuuuu!!')
elif chute > numero:
    print('Este número é maior que o correto, digite outro')
elif chute < numero:
    print('Este número é menor, digite outra vez')

# **** MODO 02 para apresentar compração e acerto

numero = int(7)
chute = int(input('digite um numero sem virgula: \n'))
    print(f'Você digitou: {chute}')

acertou = chute == numero
maior = chute > numero
menor = chute < numero

if(acertou):
    print('muito bemm..acertou!!')
elif(maior):
    print('hummm... este numero é maior!!!')
elif(menor):
    print('humm... este numero é menor.')