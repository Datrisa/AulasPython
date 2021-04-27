#calcular duas notas e ter a média

nome = input('Qual o seu nome? ')
n1 = float(input('Sua nota na Prova 1 foi: '))
n2 = float(input('Coloque também a nota da Prova 2: '))
m = (n1+n2)/2
print(f'{nome}, Sua média na matéria foi: {m}')
print('Muito bem!')

# *****************

#Dobro, Triplo e raiz quadrada

n=int(input('Digite um número: '))
d = n*2
t = n*3
rq = n**(1/2)
print(f'O dobro deste número é {d}, o triplo {t} e a raiz quadrada {rq}!')
print('Muito Obrigada, vc está me ajudando a testar :)')

# ****************

#antecessor e sucessor

n = int(input('Digite um número: '))
a = n - 1
s = n + 1
print(f'O antecessor desse número é {a} e o sucessor é {s}')
input('Pressione ENTER para Sair')
