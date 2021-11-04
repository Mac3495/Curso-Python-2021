#While
#condicion -> True -> se detiene
#condicion -> False -> sigue dando vueltas

menu = '''
====== MENU ======
1 Hamburguesa
2 Pizza
3 Alitas
4 Pollo
5 Salir
'''

switch = True

while switch:

    print(menu)

    usuario = int(input('Ingrese una opcion: '))

    texto = 'Su orden es: '

    if usuario == 1:
        print(texto, 'Hamburguesa')
    elif usuario == 2:
        print(texto, 'pizza')
    elif usuario == 3:
        print(texto, 'Alitas')
    elif usuario == 4:
        print(texto, 'Pollo')
    elif usuario == 5:
        print("Hasta pronto!!!")
        switch = False
    else:
        print("Opcion no valida")


#Listas

lista1 = ['Hamburguesa', 'Pizza', 'Pollito']
print(lista1)

lista1.append('Alitas')
print(lista1)

lista1 += ['Jugos', 'Soda']
print(lista1)

print(lista1[4])

lista1[1] = 'Nuggets'
print(lista1)

lista1.insert(2, 'Pizza')
print(lista1)

lista1.remove('Pollito')
print(lista1)

lista1.reverse()
print(lista1)

