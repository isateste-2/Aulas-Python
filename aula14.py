#  format é uma funcao como se fosse uma matriz
#ele executa os valores na ordem definida, e quando ultra
# ultrapassa essa quantidade de valores, da erro no codigo

a = 'A'
b = 'B'
c= 1.1

string= 'a ={}  b={}  c= {}'
formato = string.format(a,b,c)
#a,b,c tiveram valores diefinidos no começo do codigo 
# o print deve ser a segunda funcao poisa primeira nao possui os valores declarados e sim a segunda funcao

print(formato)

#o format segue a sequencia mas se quiser utilizar de maineira alterada da declarada 
# é possivel a partir da localizacao de sequencia de caracter iniciado em 0 (zero)

string_2 = 'a ={1}  b={2:.2f}  c= {0}'
formato_2=  string_2.format(a,b,c)

print(formato_2)

# da para declara a quantidade de casas desejadas dentro do couchetes do argumento


