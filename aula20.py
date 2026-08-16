primeira_valor = int(input('digite um valor: '))
segundo_valor = int(input('Digite outro valor: '))

if (primeira_valor > segundo_valor):
    print(f'o primeiro valor = {primeira_valor} é maior que o segundo valor = {segundo_valor}')

elif (primeira_valor == segundo_valor):
    print(f'digitou os valores iguais, {primeira_valor} = {segundo_valor}')

else:
    print(f'o segundo valor = {segundo_valor} é maior que o primeiro valor = {primeira_valor}')