def main():
    """
    Verificar si un número es múltiplo de 5
    """

    num = int(input("Ingrese un número: "))

    if num % 5 == 0:
        print(True)
    else:
        print(False)

if __name__=='__main__':
    main()
