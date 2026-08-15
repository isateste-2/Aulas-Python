#if / elfi/ else
#SE / SE NAO SE / SE NAO
    
condicao1= False
condicao2= False
condicao3= False
condicao4= False 

if condicao1:
    print ("codigo para condicao 1")

elif condicao2:
    print("codigo para condicao 2")

elif condicao3:
    print("codigo para condicao 3")

elif condicao4:
    print("codigo para condicao 4")

else:
    print('nenhuma condicao foi satisfeita')

#mesmo se todas sao verdadeiras, apenas a primeira condicao sera executada, pois o if e lido de cima para baixo e finalizado
#assim que uma condicao for satisfeita, o restante do codigo nao sera lido