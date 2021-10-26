#Estructuras de control IF

edad_juan = 25
edad_ariel = 17
dinero_juan = 50
dinero_ariel = 200

print("===== FIESTA =====")
print('Juan es mayor de edad?', edad_juan >= 18)
print('Ariel es mayor de edad?', edad_ariel >= 18)

print("==================")

if edad_juan >= 18:
    if dinero_juan >= 100:
        print("Entra a la fiesta!!!")
    else:
        print("NOOO entra a la fiesta!!! Le falta dinero")
else:
    print("NOOO entra a la fiesta!!!")


#SWICH

menu = '''
====== MENU ======
1 Administrador
2 Desarrolador
3 Gerente
4 Cliente
5 Salir
'''

print(menu)

usuario = int(input('Ingrese una opcion: '))

texto = 'Bienvenid@: '

if usuario == 1:
    print(texto, 'Administrador')
elif usuario == 2:
    print(texto, 'Desarrolador')
elif usuario == 3:
    print(texto, 'Gerente')
elif usuario == 4:
    print(texto, 'Cliente')
elif usuario == 5:
    print("Hasta pronto!!!")
else:
    print("Opcion no valida")

#Ciclos
#For, While

#rango = range(1,10)
#print(rango)

#for valor in rango:
#    print(valor)

lista_de_numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


for numero in lista_de_numeros:
    if numero % 2 == 0:
        print(numero, "es par")

