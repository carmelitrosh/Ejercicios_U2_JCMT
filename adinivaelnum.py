# adinivaelnum.py
print("Adivino un múmero del 1-10")
print("José Moya -- GDS0151 \n")
import random

numero = int(input("Escriba un número entero: "))

numrandom= random.randint(1, 10)

if numero == numrandom:
     print("Felicidades, adivinaste el número.")
else:
     print("Lo siento, intentalo de nuevo.")
