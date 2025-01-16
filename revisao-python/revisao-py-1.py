
notas = {
    'joão' : [9.3, 8.5, 10, 8],
    'Ana' : [9.5, 9, 9.3, 8.5],
    'marcelo' : [9, 9.5, 8.2, 9]
}

print('A soma das notas de Ana será: ', sum(notas['Ana']) / len(notas['Ana']))

for chave, valor in notas.items():
    print(f'{chave}:{valor}')

for aluno in notas:
    print(f'A média do {aluno} será: ', sum(notas[aluno]) / len(notas[aluno]))