import os
import modules.biblioAdmin as books

biblioteca = [['Base de datos',[]],['Fundamentos',[]],['Programacion',[]],['Frontend',[]],['Backend',[]]]

opcion = 0

title = """
-------------------------------------------
+ SISTEMA DE GESTION DE LIBROS CAMPUSLAND +
-------------------------------------------
"""
menu = "1. Agregar libro\n2. Buscar Libro\n3. Movimientos\n4. Dar de baja\n5. Salir"
menuMovimientos = "1. Prestar Libro\n2. Devolver libro\n3. Ir menu Principal"

while (opcion < 5):
    os.system('cls')
    print(title)
    print(menu)
    opcion = int(input(":) "))
    match opcion:
        case 1:
            books.AddBook(biblioteca)
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            print("Vuelve pronto......")
            os.system('pause')
        case _:
            print("La opcion ingresada no es valida.....")
            os.system('pause')
            opcion=0