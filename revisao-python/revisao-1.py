#revisao de dicionário

while True:
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    cidade = input('Digite sua cidade: ')
    break

perfil = {
    'nome' : nome,
    'idade' : idade,
    'cidade': cidade
}

for chave, valor in perfil.items():
    print(f'{chave} : {valor}')