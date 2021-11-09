#funciones -> devolver algo o no -> metodo
#PEP8
import tkinter as tk

lista_de_frutas = []

root = tk.Tk()

fruta_agregada = tk.StringVar()
fruta_buscada = tk.StringVar()
fruta_vendida = tk.StringVar()
mensaje = tk.StringVar()

sw = False

def mostrar_frutas():
    if len(lista_de_frutas) == 0:
        print('No hay frutas')
        mensaje.set('No hay frutas')
    else:
        print(lista_de_frutas)
        mensaje.set(lista_de_frutas)

def agregar_fruta():
    fruta = fruta_agregada.get()
    lista_de_frutas.append(fruta)
    mensaje.set('Fruta Agregada!')
    print('Fruta Agregada!')
    fruta_agregada.set('')

def fruta_existente(fruta):
    if fruta in lista_de_frutas:
        return True
    else:
        return False

def buscar_fruta():
    fruta_buscar = fruta_buscada.get()
    if fruta_existente(fruta_buscar):
        mensaje.set('Fruta disponible')
        fruta_buscada.set('')
        print('Fruta disponible')
    else:
        mensaje.set('Fruta no disponible')
        fruta_buscada.set('')
        print('Fruta no disponible')

def vender_fruta():
    fruta_vender = fruta_vendida.get()
    if fruta_existente(fruta_vender):
        mensaje.set('Fruta vendida!')
        print('Fruta vendida!')
        lista_de_frutas.remove(fruta_vender)
        fruta_vendida.set('')
    else:
        mensaje.set('Fruta no disponible')
        print('Fruta no disponible')
        fruta_vendida.set('')

def salir():
    print("Hasta pronto!!!")
    global sw
    sw = False

def opcion_no_disponible():
    print("Opcion no valida")

root.geometry('800x500')
root.title('Tiendita de frutas')
root.configure(bg="#009688")

tk.Label(root, text='TIENDITA DE FRUTAS', bg="#009688", fg='white', font=('', 32)).place(x=250, y=30)

#Mostrar Frutas
tk.Label(root, text='MOSTRAR FRUTAS', bg="#009688", fg='white', font=('', 24)).place(x=30, y=120)
tk.Button(root, text='Mostrar', bd=0, command=mostrar_frutas).place(x=240, y=120)

#Agregar
tk.Label(root, text='AGREGAR FRUTA', bg="#009688", fg='white', font=('', 24)).place(x=30, y=170)
tk.Entry(root, justify='center', textvariable=fruta_agregada).place(x=250, y=170)
tk.Button(root, text='Agregar', bd=0, command=agregar_fruta).place(x=500, y=170)

#Buscar
tk.Label(root, text='BUSCAR FRUTA', bg="#009688", fg='white', font=('', 24)).place(x=30, y=230)
tk.Entry(root, justify='center', textvariable=fruta_buscada).place(x=250, y=230)
tk.Button(root, text='Buscar', bd=0, command=buscar_fruta).place(x=500, y=230)

#Vender
tk.Label(root, text='VENDER FRUTA', bg="#009688", fg='white', font=('', 24)).place(x=30, y=290)
tk.Entry(root, justify='center', textvariable=fruta_vendida).place(x=250, y=290)
tk.Button(root, text='Vender', bd=0, command=vender_fruta).place(x=500, y=290)

tk.Label(root, textvariable=mensaje, bg="#009688", fg='white', font=('', 24)).place(x=300, y=410)
tk.Button(root, text='Salir', bd=0, command=root.destroy).place(x=400, y=450)
root.mainloop()

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