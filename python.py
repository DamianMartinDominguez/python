#ejemplos while con break
palabrita = "palabra"

while palabrita:
    palabrita= str(input("ingrese una palabra: "))
    if palabrita == "chupacabra":
        print("Has dejado el bucle con exito")
        break
