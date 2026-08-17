'''Formatação basica de strings

s- string
d - int
f - float
.<numero de digitos>f
x ou X - hexadecimal
(caractere)(><^)(quantidade)
> - esquerda
< - direita
^ - centro
Sinal - + ou -
conversion flags  -!r !s !a'''

variavel = 'ABC'
print(f'{variavel}.')
print(f'{variavel: >10}.')
print(f'{variavel: <10}.')
print(f'{variavel:$^10}')