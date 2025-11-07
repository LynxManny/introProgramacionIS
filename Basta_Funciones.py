import random

def elegir_palabra(palabras):
    return random.choice(palabras)

def inicializar_progreso(palabra):
    return ["_"] * len(palabra)

def mostrar_estado(progreso, vidas):
    print("Palabra:", " ".join(progreso))
    print("Vidas restantes:", vidas)

def validar_letra(letra):
    return len(letra) == 1 and letra.isalpha()

def actualizar_progreso(palabra, progreso, letra):
    return [letra if palabra[i] == letra else progreso[i] for i in range(len(palabra))]

def jugar(palabra, progreso, vidas):
    if vidas == 0:
        print("Te quedaste sin vidas. La palabra era:", palabra)
        return
    if "_" not in progreso:
        print("¡Felicidades! Adivinaste la palabra:", palabra)
        return
    
    mostrar_estado(progreso, vidas)
    letra = input("Dime una letra: ").lower()

    if not validar_letra(letra):
        print("Solo una letra nada más.\n")
        return jugar(palabra, progreso, vidas)

    if letra in palabra:
        print("¡Correcto! La letra está en la palabra.\n")
        nuevo_progreso = actualizar_progreso(palabra, progreso, letra)
        return jugar(palabra, nuevo_progreso, vidas)
    else:
        print("Error. Letra incorrecta. Pierdes una vida.\n")
        return jugar(palabra, progreso, vidas - 1)

#Inicio del juego
print("¡BIENVENIDO AL JUEGO DEL AHORCADO!")
print("Adivina la palabra del animal. Solo tienes 3 vidas.\n")

palabras = ["zorro", "elefante", "jirafa", "gato", "ballena", "raton"]
palabra_secreta = elegir_palabra(palabras)
progreso_inicial = inicializar_progreso(palabra_secreta)
vidas_iniciales = 3

jugar(palabra_secreta, progreso_inicial, vidas_iniciales)
