# tablasdemultuplicar.py
print("Tablas de multiplicar")
print("José Moya -- GDS0151 \n")
def imprimir_tabla(numero):
    contador = 1
    while contador <= 10:
        resultado = contador * numero
        print("{} x {} = {}".format(numero, contador, resultado))
        contador = contador + 1

i =1
while i<=10:
    imprimir_tabla(i)
    i += 1
    
