nome=input('Digite seu Nome:\n ').upper()
print('Olá',nome, 'Você é benvindo!! \nPreciso de informações para calcular seu IMC,\nPor favor utilize PONTO e não vírgula')
peso=float(input('  Qual seu Peso? \n'))
altura=float(input('  Qual sua altura?\n'))
resultado=(peso/(altura*altura))
print('{:.2f}'.format(resultado))
print('{}Seu ICM é: {:.2f}\n'.format(nome,resultado))

if (resultado <= 16):
    print('     Magreza Grave, tem que se cuidar')
elif (resultado <=17) :
    print('     Magreza Moderada, fique atento(a)')
elif (resultado <=18.50):
    print(      'Magreca Leve, fique atento(a)')
elif (resultado <= 25) :
    print ('        Parabéns, você está saudável!!')
elif (resultado <= 30):
    print('     Pequeno Sobrepeso, não vacile!!')
elif (resultado <=35):
    print('     Obesidade Grau 1, não abuse!!')
elif (resultado <= 40):
    print('     Obesidade Grau 2, tem que se cuidar')
else:
    print('     Obesidade Grau 3, está precisando emagrecer urgente')

tabela = input('Deseja ver nossa Tabela de IMC?? S ou N \n').upper()
if (tabela == "S"):
    print('a tabela toda')
else:
    print('Obrigado por Participar!!!')


