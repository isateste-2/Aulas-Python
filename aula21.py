# operadores logicos
# and (e)  or (ou)  not(nao)
# and - Todas as condicoes precisam ser verdadeiras

# Se qualqur valor for considerador falso, a expressao inteira sera avaliada naquele valor

# Sao consideradors falsy (que vc ja viu)
# 0 0.0 '' False

# Tambem existe o tipo None que é usado para representar um nao valor

'''entrada = input("[E]ntrar [S]air: ")
senha_digitada = input("senha: ")

senha_perimitida = '123456'


if entrada == 'E' and senha_digitada == senha_perimitida:
    print('Entrar')

else:
    print("sair")'''


print(True and False and True) #avaliaçao em curto circito
print(bool(0))
print(bool(0.0))
print(bool(''))
print(True and 0 and True) 

'''if 0 and 1:
    print(True and 1)''' #if considerado como falsy portanto if nao sera executado

if 1 and 1:
    print(True and 1 and False)