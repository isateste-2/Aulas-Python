#if / elif  / else
#se/ se nao se / se nao 

entrada = input('voce quer "entrar" ou "sair"?')

#para locarlizarmos que o usuario esta indicando é necessario um if
#o if é lida pela hierarquia do tab

if entrada == 'entrar':
    print('voce entrou no sistema')

#elfi pode executado varias vezes
#serve como segunda opção
elif entrada == 'sair':
    print("voce saiu do sistema")

else:
    print("voce nao digitou nem entrar e nem sair")