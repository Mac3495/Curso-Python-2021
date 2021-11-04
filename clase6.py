#funciones -> devolver algo o no -> metodo
#PEP8

lista_de_frutas = []

sw = True

def mostrar_frutas():
    if len(lista_de_frutas) == 0:
        print('No hay frutas')
    else:
        print(lista_de_frutas)

def agregar_fruta():
    fruta = input('Ingrese la fruta: ')
    lista_de_frutas.append(fruta)
    print('Fruta Agregada!')

def fruta_existente(fruta):
    if fruta in lista_de_frutas:
        return True
    else:
        return False

def buscar_fruta():
    fruta_buscar = input('Ingrese la fruta: ')
    if fruta_existente(fruta_buscar):
        print('Fruta disponible')
    else:
        print('Fruta no disponible')

def vender_fruta():
    fruta_vender = input('Ingrese la fruta: ')
    if fruta_existente(fruta_vender):
        print('Fruta vendida!')
        lista_de_frutas.remove(fruta_vender)
    else:
        print('Fruta no disponible')

def salir():
    print("Hasta pronto!!!")
    global sw
    sw = False

def opcion_no_disponible():
    print("Opcion no valida")

menu = '''
====== MENU ======
1 Mostrar Frutas
2 Agregar Fruta
3 Buscar Fruta
4 Vender Fruta
5 Salir
'''

while sw:
    print(menu)

    opcion = int(input('Ingrese una opcion: '))

    if opcion == 1:
        mostrar_frutas()
    elif opcion == 2:
        agregar_fruta()
    elif opcion == 3:
        buscar_fruta()
    elif opcion == 4:
        vender_fruta()
    elif opcion == 5:
        salir()
    else:
        opcion_no_disponible()