# paresoimpares.py
print("Calcular si un número es par o impar")
print("José Moya -- GDS0151 \n")

def main():
    numero_1 = int(input("Escriba un número entero: "))

    if numero_1 % 2 == 0:
         print("El número es par.")
    else:
         print("El número es impar.")


if __name__ == "__main__":
    main()
