# Revisão Geral


# Variáveis

caixa = 'dado' 


# Tipos de dados primitivos

## strings

nome = 'Johel'
aluno = 'João'
time = 'Cuiabá'
cpf = '12312312312'

## integer (int)

idade = 25
gols = 5
estoque = 50

## float

nota = 7.5
saldo = 3253.27
temp = 25.3
media_de_gols = 5.3

## boolean

condicao = False
ligado = True
time_venceu = False
esta_chovendo = False
acima_da_media = True

# operações básicas com números

soma = idade + 3

subtracao = nota - 5

multiplicacao = 25 * 4

divisao = 7 / 2

divisao_inteira = 7 // 2

resto = 7 % 2 # módulo da divisão

potencia = 3**3

# operações com strings


# transformação de tipos

str(5)
int('7')
float('19.5')


# Estruturas condicionais (if, elif, else)

if nota >= 5:
    print('Aluno aprovado!')
else:
    print('Aluno reprovado!')


if time == 'Cuiabá' and time_venceu:
    print('Legal! Parabéns')
else:
    print('Perdeu')


if nota > 9:
    print('Seu conceito é A')
elif nota > 8:
    print('Seu conceito é B')
elif nota > 7:
    print('Seu conceito é C')
else:
    print('Seu conceito é D')


# Estruturas de repetições (for, while)

# for - permite iterar por conjuntos de dados, como range, listas, tuplas, strings 

for n in range(1, 11):
    # print('5 x', n, ' =', n*5)
    # print('5 x ' + str(n) + ' = ' + str(n*5))
    print(f'5 x {n} = {n*5}')


# while - permite repitir um código enquanto uma condição é satisfeita

#while condicao:
    # faça isso

n = 1
while n <= 10:
    print(f'7 x {n} = {n*7}')
    n += 1

print('=======================')

# while True:
#     print('1 - soma')
#     print('2 - subtração')
#     print('3 - sair')
#     entrada = input('Digite uma opção: ')
#     if entrada == '1':
#         num1 = input('Digite o primeiro número: ')
#         num2 = input('Digite o segundo número: ')
#         print(f'{int(num1) + int(num2)}')
#     elif entrada == '2':
#         num1 = int(input('Digite o primeiro número: '))
#         num2 = int(input('Digite o segundo número: '))
#         print(f'{num1 - num2}')
#     elif entrada == '3':
#         print('Você saiu do menu')
#         break




# Funções

## chamando funções

# nome_da_funcao(argumentos)

print('Olá, essa é a função print')
print(type(nome))
print(len(nome))

print('======================')

# criar funções
def nome_da_funcao(argumento1, argumento2):
    print(argumento1 + argumento2)


def soma(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

resultado = soma(7, 3)
print(resultado)

print(soma(9, 4))



# módulos e bibliotecas

# internas
import math as m

raiz = m.sqrt(9)
print(raiz)

# exemplos:
# math, datetime, re, random

# externas:

# pip install nome_da_biblioteca
# exemplos: rich, pandas



# manipulação de strings

print(time)
print(time.upper())

# fatiamento de strings:
print(time[1:4])

cpf = '12312312312'
print(cpf[0:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:])

# verifique no portal o execício1.pdf


# Coleções de dados

## listas []

alunos = ['João', 'Marcelo', 'Ana', 'Regina', 'Gustavo']

lista1 = [1, 2, 5, 8, 3 , 8]
lista2 = [1, 2, True, 'texto', 2.5]

print(alunos[1])
print(alunos[-1])

# fatiamento de listas
print(alunos[1:3])

### manipulação de listas

# verifique no portal o arquivo Métodos de Manipulação de Listas

alunos.append('Came')
print(alunos)

alunos.append('Arthur')

if 'Arthur' in alunos:
    print('Arthur está presente')
else:
    print('Arthur não está presente')


for aluno in alunos:
    print(aluno)

for index, item in enumerate(alunos):
    print(f'{index} - {item}')

## tuplas ()

tupla = (1, 3, 7)
coordenadas = (23.47823, 11.34234)


## dicionários {'chave': 'valor'}

usuario = {
    'nome': 'Johel',
    'email': 'johel@exemplo.com',
    'cpf': '12312312312',
    'idade': 25,
    'admin': True
}

produto = {
    'nome': 'IPhone',
    'modelo': 7,
    'memória': '64gb',
}

print(usuario['email'])

for chave, valor in usuario.items():
    print(f"{chave}: {valor}")



## dados aninhados


print('======================================')



matriz = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
    ]


print(matriz[0][-1])


lista_de_tuplas = [(4, 6), (2, 5), (1, 7), (81, 23)]

print(lista_de_tuplas[1][1])


notas_de_alunos = {
    'João': [9.3, 8.5, 10, 8],
    'Ana': [9.5, 9, 9.3, 8.5],
    'Marcelo': [9, 9.5, 8.2, 9]
}

print(notas_de_alunos['João'])
# print('A média das notas do João é:', sum(notas_de_alunos['João']) / len(notas_de_alunos['João']))


for aluno in notas_de_alunos.keys():
    print(f'A média das notas do {aluno} é:', sum(notas_de_alunos[aluno]) / len(notas_de_alunos[aluno]))



produtos = [
    {
    'nome': 'IPhone',
    'modelo': 7,
    'memória': '64gb',
    },
    {
    'nome': 'Smartwatch',
    'modelo': 'XS',
    'memória': '4gb',
    },
    {
    'nome': 'Sansung Galaxy',
    'modelo': 'S20',
    'memória': '64gb',
    }
]

usuarios = [
    {
    'nome': 'Johel',
    'email': 'johel@exemplo.com',
    'cpf': '12312312312',
    'idade': 25,
    'admin': True,
    'endereco': {
        'rua': 'X',
        'numero': 15,
        'cidade': 'Cuiabá',
        'coordenadas': (13.43243, 20.34343)
        }
    },
    {
    'nome': 'João',
    'email': 'joao@exemplo.com',
    'cpf': '12312312313',
    'idade': 25,
    'admin': False
    },
    {
    'nome': 'José',
    'email': 'jose@exemplo.com',
    'cpf': '12312312314',
    'idade': 26,
    'admin': False
    },
]


latitude = usuarios[0]['endereco']['coordenadas'][0]
longitude = usuarios[0]['endereco']['coordenadas'][1]


print(f'A latidute do usuário Johel é {latitude}, e a longitude é {longitude}')