def main():
    """
    Comprobar si una temperatura está en un rango aceptable entre 18 y 25 grados Celsius.
    """

    temperatura = float(input("Ingrese la temperatura: "))

    if temperatura >= 18 and temperatura <= 25:
        print("Tempartura aceptable")
    else:
        print("Termpartura fuera de rango")

if __name__=='__main__':
    main()
