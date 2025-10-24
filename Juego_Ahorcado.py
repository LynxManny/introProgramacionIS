import random

palabras = ["zorro", "elefante", "jirafa", "gato", "ballena", "raton"]

palabra_secreta = random.choice(palabras) #Eleccion de palabra random

progreso = ["_"] * len(palabra_secreta)
vidas = 3

print("¡BIENVENIDO AL JUEGO DEL AHORCADO!")
print("Adivina la palabra del Animal. Solo tienes 3 vidas.\n")

while vidas > 0 and "_" in progreso:
    print("Palabra: ", " ".join(progreso))
    print("Vidas restantes:", vidas)
    letra = input("Dime una letra: ").lower()

    if len(letra) != 1 or not letra.isalpha():
        print("Solo una letra nada mas.\n")
        continue

    if letra in palabra_secreta: # Revision si la letra está en la palabra
        print("¡Correcto! La letra está en la palabra.\n")
        for i in range(len(palabra_secreta)):
            if palabra_secreta[i] == letra:
                progreso[i] = letra
    else:
        vidas -= 1
        print("Error Letra incorrecta.\n Pierdes una vida.\n")

if "_" not in progreso: #Fin del juego
    print("¡Felicidades! Adivinaste la palabra:\n", palabra_secreta)
else:
    print("Te quedaste sin vidas. La palabra era:", palabra_secreta)

