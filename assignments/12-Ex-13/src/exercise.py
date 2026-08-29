def main():
    """
    Verificar si 3 números pueden formar un triángulo
    """

    lado1 = float(input("Ingrese el primer lado: "))
    lado2 = float(input("Ingrese el segundo lado: "))
    lado3 = float(input("Ingrese el tercer lado: "))

    if lado1 >0 and lado2 >0 and lado3 >0 and \
        lado1 +lado2 >lado3 and lado1 +lado3 >lado2 and lado2 +lado3 >lado1:
        print("Forma un triángulo")
    else:
        print("No forma un triángulo")

if __name__=='__main__':
    main()
