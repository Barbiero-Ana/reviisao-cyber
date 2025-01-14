# * Revisão geral * #

# Váriaveis
- São dados aos quais podem ser atribuidos valores, informações etc
ex: caixa = 'dado' -> ela está armazenando um dado

# Strings
- Váriaveis de texto (str)
nome = 'nome' 
aluno = 'ana'
- Para ser armazenado um dado do tipo texto é preciso colocar entre ''

# Inteiros (INT)  Váriaveis do tipo Inteiro
- idade = 23
- gols = 10
- Armazenamento de dados numéricos do tipo inteiro dentro de uma variável 

# Float (Números reais) - Ocupam mais espaço de memória
- saldo = 90.88
- temperatura = 34.5
- nota = 3.6
- media_gols = 5.5

# Booleans - Dados lógicos
- Se não atender as condições será o inverso
- Sempre por o True ou False com letra maiúscula
- ligado = True
- time_venceu = True
- chovendo = False

# Operações básicas com números
- * -> multiplicação
- ** -> potenciação (são dois asterisco '**')
- / -> divisão
- + -> soma (+)
- - -> subtração (-)
- // -> divisão inteira
- % -> resto da divisão (módulo)
* Para mais operações, utilizar a biblioteca *Math* - no começo do código adicionar *import math* *


# Manipulação de Strings (STR)
- nome = 'Python' -> Atribuição de uma string
- saudacao = 'olá' + nome -> concatenação de strings
- print(saudacao) -> irá printar na tela o texto armazenado na variável de saudacao + o nome dentro da variével de nome
- print(nome * 3) -> Repete a string (o nome presente na variável)
- print(time.upper())
* Fatiamento de strings
- print(time[1:4])

# Verificar no portal as formas de manipulação de string - Estudar e revisar*

# Comparadores lógicos
- == (igual a)
- != (diferente de)
- > (maior que)
- < (menor que)
- >= (maior ou igual)
- <= (menor ou igual)


# Estruturas de condicionais (if, elif, else) 
- Elif = else porém com possibilidade de condição
- if nota >= 5:
    - *executar condição proposta pelo código*
- Define uma condição lógica para que o código siga e siga organizado conforme a condição
- Possível definir duas condições em uma só condicional fazendo uso de booleanos
if time == 'cuiabá' *and* time_venceu:
    print('Parabéns!')
- *and* (e) é um dado booleano (and, or, not (e, nao, ou))

- Utilizável em sistemas de notas, bancos entre outros

* if nota > 9:
    print('Seu conceito é A')
elif nota > 8:
    print('Seu conceito é B')
elif nota > 7:
    print('Seu conceito é C')
else:
    print('Seu conceito é D') 
* 

# Estruturas de repetição (for, while)
- Serve para realizar atividades que ocorrem de forma repetitiva no código a fim de deixa-lo mais organizado e lógico
- por ex: preencher uma tabuada de forma mais prática e lógica
- For: permite interar (passar várias vezes) por conjuntos de dados, como range, listas, tuplas, strins(str)
- Range(*inserir intervalo desejado ou número de repetições*) - Cria uma lista com o intervalo de valores proposto dentro dos ()
* for i in range(1, 11):
    print(f'5 X {i} = {5 * i}')

- While (enquanto)
- Permite repetir um código enquanto uma condição é satisfeita
* while *condicao*:
    *executar codição proposta pelo código*

* n = 1
while n >= 10:
    print(f' 5 X {n} = {5 * n}')
    n += 1

* while True:
    menu = input('s/n para continuar: ')

    if menu == 's':
        *executar código*
    elif menu == 'n':
        print('Até a próxima')
        break -> *O break interrompe o código dentro do while e cai fora do laço de repetição*
    else:
        print('Opção inválida! Tente novamente')

# Funções
- bloco de códigos que podem ser maiores e logo depois podem ser importados para um 'main.py' - deixando o código mais organizado e fluido
- Possível chamar a função para deixar o código mais limpo
*funções nativas do próprio python*
- print()
- print(type(nome)) - retorna o tipo da váriavel
- print(len(nome)) - retorna a quantidade de caracteres/ items dentro da váriavel

# Cria funções
- def nome_da_funcao(argumento1, argumento2):
    print(argumento1 + argumento2 )

- def soma(num1, num2):
    return num1 + num2

# Módulos e bibliotecas
- ex: *import math*
- útil para facilitar o trabalho individual ou da equipe
- Facilitar e agilizar o código (codar)
- Possível sua importação como alias (apelido)
- ex: *import math as m*

# Bibliotecas externas
- módulos e bibliotecas que necessitam de instalção por meio do 'pip install nome da biblioteca'
- ex: rich, pandas, etc.

# Bibliotecas internas
- Já presentes dentro do próprio python, sem necessidade de instalação
- ex: math, datetime, re, random, etc.

# Listas []
- O indice de uma lista começa sempre em 0
- alunos = ['joao','ana','marcelo','regina','gustavo']
- print(alunos)
- lista pode adicionar tipos diferentes de dados
- para um print enumerado
* for index, item in enumerate(alunos):
    print(f'{index} : {items}')


# Fatiamento de listas
- print(alunos[1:3])

# Tuplas()
- possível mistura de tipos de dados
- Uma lista imutável 
- ex: tupla = (1, 3, 7)
- ex: coordenadas = (23.47823, 11.342234)

# Dicionários - {'chave' : 'valor' }
- ex: usuario = {
    'nome' : 'Johel',
    'email' : 'johel@exemplo.com',
    'cpf' : '123456789-10',
    'idade' : 25,
    'admin' : True
}

- ex: produto = {
    'nome' : 'Iphone',
    'modelo' : 7,
    'memoria' : '64gb',
}

- para buscar uma informação do dicionário faz-se:
* print(usuario['email'])

- Como dar um print mais 'organizado' do dicionário
* for chave, valor in usuario.items():
    print(f'{chave}: {valor}')

# Dados aninhados
- 
