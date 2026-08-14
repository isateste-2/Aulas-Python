# nessa aula é explicado que o f antes da sequencia de string é possivel formatar
# a sequencia se variaveis 

nome='isadora soares' 
idade= 20
altura= 1.70
peso= 74
imc = peso/ altura ** 2

'f-string'
linha_1 = f'{nome} tem {idade} anos e pesa {74} kg, ela tem {altura},'
linha_2= f'seu imc é {imc}'

print(linha_1)
print(linha_2)

# em python é só colocar : para o print no if/else

if(imc <= 24.9): print('esta peso ideal')
else : print('esta acima do peso')