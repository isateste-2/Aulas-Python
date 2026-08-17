'''operador logico
    or - qualquer condiçao verdadeira avalia toda a expressao como verdadeira

    se qualquer valor for considerado como verdadeiro a expressao inteira sera 
    avaliada naquele valor.

    sao considerado falsy 
    0 0.0 '' False

    existe o None para um nao valor'''

'''entrada = input("[E]ntrar ou [S]air: ")
senha_digitada= input('Senha: ')

senha_permitida = '123456'

if entrada == 'E' or entrada =='e' and senha_digitada == senha_permitida:
    print("Entrar")

else:
    print("Sair")'''

print(True or False)
print(0 or False or 'abc')
#ele ignora todos os falsos e mostra somente o verdadeiro

print(False or True)
print(False or False)

senha = input('senha: ') or 'sem senha'
print(senha)