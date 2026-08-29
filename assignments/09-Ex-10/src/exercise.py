def main():
    """
    Determinar si un número es múltiplo de 3 y 5
    """

    num = int(input("Ingrese un número: "))

    if num % 3 == 0 and num % 5 == 0:
        print("Múltiplo de 3 y 5")
    else:
        print("No es múltiplo de 3 y de 5")

if __name__=='__main__':
    main()
