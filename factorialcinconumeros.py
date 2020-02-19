# factorialcinconumeros.py
import math

print("Factorial de 5 numeros")
print("José Moya -- GDS0151 \n")

i=1
while i <=5:
    fact=float (input("Ingresa un numero: \n" ))
    resultado = (math.factorial(fact))
    print(str(resultado))
    i += 1
