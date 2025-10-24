from random import choice
from time import sleep
from os import system

categorias = {}
letras = "abcdefghijklmnopqrstuvwxyz"
puntosTotales = 0
contadorRondas = 0

print("\n---¡Bienvenido al asistente del juego Basta!---")
print("Agrega las categorías de tu juego Basta\n")
contadorCategoria = 0
while True:
    contadorCategoria += 1
    categoria = input("Escribe la categoría y/o deja un vacío teclea ENTER para salir): ")
    if categoria == "":
        contadorCategoria -= 1
        break
    categorias[contadorCategoria] = categoria.capitalize()

if contadorCategoria == 0:
    print("\nNo se escribio ninguna categoría. Fin del programa.")
    exit()

sleep(1)
system("cls")

while True:
    contadorRondas += 1
    #Elegir una letra random del abecedario
    letra = choice(letras)
    letras = letras.replace(letra,"")
    print(f"\n¡Comienza la ronda {contadorRondas}, con la letra: {letra.upper()}!")
    valoresCategorias = categorias.values()
    print("Categorías: ", ", ".join(map(str, valoresCategorias)))

    print("Pensando...")
    sleep(1)

    palabras = {} #Diccionario para almacenar las palabras que ingrese el usuario por categoría
    
    while True:
        for llave, valor in categorias.items():
            print(f"{llave}. {valor.capitalize()}")
        categoriaSeleccionada = input("\nSelecciona categoria con el número o 0 para salir: ")

        if categoriaSeleccionada == "0" or categoriaSeleccionada.isalpha():
            break
        if categoriaSeleccionada == "":
            continue
        else:
            categoriaSeleccionada = int(categoriaSeleccionada)
            palabra = input(f"\n{categorias[categoriaSeleccionada]} con la letra {letra.upper()}: ")
            palabras[categorias[categoriaSeleccionada]] = palabra.capitalize()

    print(f"\n--Tus palabras con la letra fueron {letra.upper()}--")
    for categoria, palabra in palabras.items():
        print(f"{categoria} --> {palabra.capitalize()}")

    sleep(3)
    print("\n--Ingresa tus puntos por categoría--")
    puntosRonda = 0
    for llave, categoria in categorias.items():
        puntosCategoria = input(f"Puntos obtenidos en {categoria}: ")
        if puntosCategoria == "":
            puntosCategoria = 0
        elif puntosCategoria.isnumeric():
            puntosRonda += int(puntosCategoria)
        else:
            puntosCategoria = 0

    print(f"\nPuntos Ronda: {puntosRonda}")
    puntosTotales += puntosRonda

    sleep(1)
    #system("cls") #Windows system(cls)

    continuar = input("\n¿Quieres seguir jugando? (s/n)")
    if continuar.lower() != "s":
        break

print("\nPuntos Totales: ", puntosTotales)
print("¡Adiós!")