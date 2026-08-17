'''Operadores in e not in

in significa entre e not in, nao esta entre

strings sao iteraveis = navega item por item

0 1 2 3 4 5 6
I S A D O R A
-6-5-4-3-2-1

PODEM SER COMEÇADO DO 0 AO NUMERO MAIOR OU DO NEGATIVO MAIOR AO NEGATIVO MENOR'''

nome = 'Isadora'
print(nome[4])
print(nome[-4])

print('a' in nome)
print('z' in nome)

print('a' not in nome)
print ("z" not in nome)

nome = input('Digite um nome: ')
encontra = input("Digite o que seja encontra: ")

if encontra in nome:
    print(f'{encontra} esta entre o nome {nome}')

else:
    print(f'a letra  {encontra} nao esta no nome {nome}')