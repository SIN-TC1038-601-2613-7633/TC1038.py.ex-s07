def main():
    """
    Verificar si un número es par o impar
    """

    num = int(input("Ingrese un número: "))

    if num % 2 == 0:
        print("Par")
    else:
        print("Impar")

if __name__=='__main__':
    main()
