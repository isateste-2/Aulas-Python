''' Operador Logico
 usado para inverter expressoes 
 not True = False
 not False = True'''

senha = input('Senha: ')

if not senha:
    print('vc nao digitou nada')

elif senha != '123456':
    print("Senha incorreta")

else:
    print('entrar')


print(not True)