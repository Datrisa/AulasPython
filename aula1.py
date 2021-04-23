# Calculo de IMC - Indice de Massa Corporal com tabela básica
nome=input('Digite seu Nome:\n ').upper()
print('Olá',nome, 'Você é benvindo!! \nPreciso de informações para calcular seu IMC,\nPor favor utilize PONTO e não vírgula')
peso=float(input('  Qual seu Peso? \n'))
altura=float(input('  Qual sua altura?\n'))
resultado=(peso/(altura*altura))
print('{:.2f}'.format(resultado))
print('{} Seu ICM é: {:.2f}'.format(nome,resultado))

# tabela comprativa
if (resultado <= 16):
    print('     Magreza Grave, tem que se cuidar\n')
elif (resultado <=17) :
    print('     Magreza Moderada, fique atento(a)\n')
elif (resultado <=18.50):
    print(      'Magreca Leve, fique atento(a)\n')
elif (resultado <= 25) :
    print ('        Parabéns, você está saudável!!\n')
elif (resultado <= 30):
    print('     Pequeno Sobrepeso, não vacile!!\n')
elif (resultado <=35):
    print('     Obesidade Grau 1, não abuse!!\n')
elif (resultado <= 40):
    print('     Obesidade Grau 2, tem que se cuidar\n')
else:
    print('     Obesidade Grau 3, está precisando emagrecer urgente\n')

# visualização da tabela em um PopUp
tabela = input('Deseja ver nossa Tabela de IMC?? S ou N \n').upper()
if (tabela == "S"):
    print('TABELA DE IMC (KG/M²):\n'
          '\n'
          '00 <16       = Magreza Grave\n'
          '16 < 17      = Magreza Moderada\n'
          '17 < 18,5   = Magreza Leve\n'
          '18,5 < 25   = Saudável\n'
          '25 < 30      = Sobrepeso\n'
          '30 < 35      = Obesidade Grau 1\n'
          '35 < 40      = Obesidade Grau 2 (severa)\n'
          '>= 40        = Obesidade Grau 3 (mórbida)\n'
          '     \n'

                    'Obrigado por Participar!!!')
else:
    print('Agradecemos sua participação')




