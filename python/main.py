import os
import requests
from tabulate import tabulate
from datetime import *
import pyfiglet


def iniciar():
    os.system('cls')
    while True:
        titulo = 'Control gastos'
        a = pyfiglet.figlet_format(titulo)
        print(a)
        print("===========================================")
        print(":: Escoja una de las siguientes opciones ::")
        print("===========================================")
        print("\n\t1. Registrar movimiento")
        print("\t2. Ver todos los movimientos")
        print("\t3. Buscar movimiento")
        print("\t4. Modificar movimiento")
        print("\t5. Eliminar movimiento")
        print("\t6. Salir")

        opción = input("\nIngrese una opción: ")

        os.system('cls')

        if opción == "1":
            nuevo_movimiento()
        elif opción == "2":
            mostrar_movimiento()
        elif opción == "3":
            buscar_movimiento()
        elif opción == "4":
            modifiacar_movimiento()
        elif opción == "5":
            eliminar_movimiento()
        elif opción == "6":
            break
        else:
            print("---------------")
            print("Opción inválida")
            print("---------------")


# 1. función para registrar un nuevo movimiento
def nuevo_movimiento():
    try:
        response2 = requests.get(url='http://localhost:3000/movimiento/todos')
        response2.json()

        tipo = input(
            '\nIngrese un número para el tipo de movimiento \n1- Ingreso\n2- Gasto\n')

        while tipo != "1" and tipo != "2":
            os.system('cls')
            tipo = input(
                '\nError ingrese un número entre 1 y 2 \n1- Ingreso\n2- Gasto\n')

        if tipo == '1':
            tipo = 'Ingreso'
        elif tipo == '2':
            tipo = 'Gasto'

        cantidad = input('\nIngrese la cantidad: ')
        while cantidad == '' or cantidad.isdigit() == False:
            os.system('cls')
            cantidad = input('\nError, ingrese una cantidad: ')

        fecha = solicitar_fecha()
        datos = {'tipo': tipo, 'cantidad': cantidad, 'fecha': fecha}
        respuesta = requests.post(
            url='http://localhost:3000/movimiento/registro', data=datos)

        print("="*22)
        print(respuesta.text)
        print("="*22)
        input("\npresione enter para seguir...")
        os.system('cls')

    except Exception:

        print("="*25)
        print("Error en la conección a la base de datos")
        print("="*25)
        input("\npresione enter para seguir...")
        os.system('cls')


# 2. funcion para mostrar todos los movimientos
def mostrar_movimiento():

    try:
        # ::: problem para visualizar cuando en vez de post se pone get :v :::
        response = requests.get(url='http://localhost:3000/movimiento/todos')
        datos = []

        # convierto los datos a una lista para poder usar tabulate
        for dato in response.json():
            temp = []
            for key, value in dato.items():
                temp.append(value)
            datos.append(temp)
        headers = ['id', 'tipo', 'cantidad', 'fecha']
        tabla = tabulate(datos, headers, tablefmt='fancy_grid')
        print(tabla)
        input("presione enter para seguir...")
        os.system('cls')
    except Exception:

        print("="*25)
        print("Error en la conección a la base de datos")
        print("="*25)
        input("\npresione enter para seguir...")
        os.system('cls')


# 3. Busca un libro por su 'id'
def buscar_movimiento():
    try:
        # para comprobar si está conectado a la base de datos
        response2 = requests.get(url='http://localhost:3000/movimiento/todos')
        response2.json()

        # ::: problem para visualizar cuando en vez de post se pone get :v :::
        id = input('\nIngrese el id del movimiento: ')
        
        if id == '' or id.isdigit() == False:
            os.system('cls')
            print("\n-----------------------------")
            print("::Error, valor de id no valido::")
            print("-----------------------------")
            input("\npresione enter para seguir...")
            os.system('cls')
        else:
            response = requests.get(
                url='http://localhost:3000/movimiento/buscar'+id)
            
            datos = []
            # convierto los datos a una lista para poder usar tabulate
            for dato in response.json():
                temp = []
                for key, value in dato.items():
                    temp.append(value)
                datos.append(temp)
            headers = ['id', 'tipo', 'cantidad', 'fecha']
            tabla = tabulate(datos, headers, tablefmt='fancy_grid')
            if len(datos) > 0:
                print(tabla)
            else:
                print("\n------------------------------------")
                print(":: El id del movimiento no existe ::")
                print("------------------------------------")
            input("Presione una tecla para continuar...")
            os.system("cls")
            
    except Exception:
        print("="*25)
        print("Error en la conección a la base de datos")
        print("="*25)
        input("\npresione enter para seguir...")
        os.system('cls')


# 4. Modifica un movimiento por su 'id'
def modifiacar_movimiento():

    try:
        response2 = requests.get(url='http://localhost:3000/movimiento/todos')
        response2.json()

        id = input("\nIngrese el id del movimiento a modificar: ")
        if id == '' or id.isdigit() == False:
            os.system('cls')
            print("\n-----------------------------")
            print("::Error, valor un id valido::")
            print("-----------------------------")
            input("\npresione enter para seguir...")
            os.system('cls')
    
        else:
            existe = requests.get(
                url='http://localhost:3000/movimiento/buscar'+id)

            if len(existe.json()) > 0:

                campo = input(
                    "Ingrese el campo a modificar:\n1. tipo\n2. cantidad\n3. fecha\n")
                nuevo_valor = ''
                if campo == '1':
                    campo = 'tipo'
                    nuevo_valor = input(
                        "Ingrese el nuevo tipo de movimiento \n1- Ingreso\n2- Gasto\n: ")
                    while nuevo_valor != "1" and nuevo_valor != "2":
                        os.system('cls')
                        nuevo_valor = input(
                            'Error ingrese un número entre 1 y 2 \n1- Ingreso\n2- Gasto\n')
                    if nuevo_valor == '1':
                        nuevo_valor = 'Ingreso'
                    elif nuevo_valor == '2':
                        nuevo_valor = 'Gasto'

                elif campo == '2':
                    campo = 'cantidad'
                    nuevo_valor = input("\nIngrese la nueva cantidad: ")
                    while nuevo_valor == '' or nuevo_valor.isdigit() == False:
                        os.system('cls')
                        nuevo_valor = input('\nError, ingrese una cantidad: ')

                elif campo == '3':
                    campo = 'fecha'
                    nuevo_valor = solicitar_fecha()

                datos = {'campo': campo,
                        'nuevo_valor': nuevo_valor}

                response = requests.post(
                    url='http://localhost:3000/movimiento/modificar'+id, data=datos)

                print("="*26)
                print(response.text)
                print("="*26)
                input("\npresione enter para seguir...")
                os.system('cls')
            else:
                print("\n------------------------------------")
                print(":: El id del movimiento no existe ::")
                print("------------------------------------")
                input("Presione una tecla para continuar...")
                os.system("cls")

    except Exception:
        print("="*25)
        print("Error en la conección a la base de datos")
        print("="*25)
        input("\npresione enter para seguir...")
        os.system('cls')


# 5. Elimina un movimiento por su 'id'
def eliminar_movimiento():

    try:
        response2 = requests.get(url='http://localhost:3000/movimiento/todos')
        response2.json()

        id = input("\nIngrese el id del movimiento a eliminar: ")
        if id == '' or id.isdigit() == False:
            os.system('cls')
            print("\n-----------------------------")
            print("::Error, valor un id valido::")
            print("-----------------------------")
            input("\npresione enter para seguir...")
            os.system('cls')
        
        else:
            
            existe = requests.get(
                url='http://localhost:3000/movimiento/buscar'+id)

            if len(existe.json()) > 0:
                response = requests.post(
                    url='http://localhost:3000/movimiento/eliminar'+id)
                print("="*35)
                print(response.text)
                print("="*35)
            else:
                print("\n------------------------------------")
                print(":: El id del movimiento no existe ::")
                print("------------------------------------")
                input("Presione una tecla para continuar...")
                os.system("cls")

    except Exception:
        print("="*25)
        print("Error en la conección a la base de datos")
        print("="*25)
        input("\npresione enter para seguir...")
        os.system('cls')


def solicitar_fecha():
    try:
        dia = int(input("Ingrese el día: "))
        mes = int(input("Ingrese el mes: "))
        anio = int(input("Ingrese el año: "))
        fecha = date(anio, mes, dia)

        return fecha
    except ValueError:
        os.system('cls')
        print("\n------------------------------------")
        print("::Error, ingrese una fecha valida::")
        print("------------------------------------")
        return solicitar_fecha()


if __name__ == "__main__":

    iniciar()
