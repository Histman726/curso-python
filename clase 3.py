edad=int(input("Introduzca su edad:\n"))

# Se deja la variable sin valor
respuesta=None

if edad>=18:
    print("Eres mayor de edad. Eliga una opcion\n")
    respuesta=input("\t1. ron\n\t2. tequila\n\t3. whisky\n\t4. vino\n")

    if respuesta=="1":
        print("Usted ha eligido tomar ron")
    elif respuesta=="2":
        print("Usted ha eligido tomar tequila")
    elif respuesta=="3":
        print("Usted ha eligido tomar whisky")
    elif respuesta=="4":
        print("Usted ha eligido tomar vino")
    else:
        print("Su opcion no es valida")
else:
    print("Usted es menor de edad no puede tomar alcohol1")