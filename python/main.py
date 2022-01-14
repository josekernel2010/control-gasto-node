import os
import requests
from tabulate import tabulate


def iniciar():
    os.system('cls')
    while True:

        print("Seleccione una opción:")
        print("\t1. Registrar movimiento")
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


# función para registrar un nuevo movimiento
def nuevo_movimiento():
    tipo = input('Ingrese el tipo de movimiento \n- Ingreso\n- Gasto\n')
    cantidad = input('Ingrese la cantidad: ')
    fecha = input('Ingrese la fecha: ')
    datos = {'tipo': tipo, 'cantidad': cantidad, 'fecha': fecha}
    respuesta = requests.post(
        url='http://localhost:3000/movimiento/registro', data=datos)

    print("="*22)
    print(respuesta.text)
    print("="*22)


def mostrar_movimiento():
    # ::: problem para visualizar cuando en vez de post se pone get :v :::
    response = requests.get(url='http://localhost:3000/movimiento/todos')
    datos = []
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


# 3. Busca un libro por su 'id'
def buscar_movimiento():
    # ::: problem para visualizar cuando en vez de post se pone get :v :::
    id = input('Ingrese el id del movimiento: ')
    response = requests.get(url='http://localhost:3000/movimiento/buscar'+id)
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


def modifiacar_movimiento():
    id = input("Ingrese el id del movimiento a modificar: ")
    campo = input(
        "Ingrese el campo a modificar:\n1. tipo\n2. cantidad\n3. fecha\n")
    nuevo_valor = ''
    if campo == '1':
        campo = 'tipo'
        nuevo_valor = input("Ingrese el nuevo tipo de movimiento: ")
    elif campo == '2':
        campo = 'cantidad'
        nuevo_valor = input("Ingrese la nueva cantidad: ")
    elif campo == '3':
        campo = 'fecha'
        nuevo_valor = input("Ingrese la nueva fecha: ")
    datos = {'campo': campo, 'nuevo_valor': nuevo_valor}
    response = requests.post(
        url='http://localhost:3000/movimiento/modificar'+id, data=datos)
    print("="*26)
    print(response.text)
    print("="*26)


def eliminar_movimiento():
    id = input("Ingrese el id del movimiento a eliminar: ")
    response = requests.post(
        url='http://localhost:3000/movimiento/eliminar'+id)
    print("="*35)
    print(response.text)
    print("="*35)


iniciar()
