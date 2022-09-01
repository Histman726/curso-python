error=input("Introduzca el error:\n")

match error:
    case "200":
        print("Todo OK")
    case "301":
        print("Movimiento permanente en la pagina")
    case "302":
        print("Movimiento temporal en la pagina")
    case "404":
        print('Pagina no encontrada')
    case "500":
        print('Error interno en el servidor')
    case "503":
        print("Servicio no disponible")
    case _:
        print("No hay errores")