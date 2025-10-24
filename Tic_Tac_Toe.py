import random

# Imprime el tablero 3x3
tablero = [[" " for _ in range(3)] for _ in range(3)]

# Combinaciones ganadoras (posiciones lineales del 0 al 8)
ganadoras = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # En Filas
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # En Columnas
            (0, 4, 8), (2, 4, 6)              # En Diagonales
            ]

print("=== BIENVENIDO AL JUEGO TIC TAC TOE ===\n")
print("Las posiciones del tablero son:")
print("""
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
    """)

# Elige el modo de juego
modo = input("Modo de juego:\n 1). Contra otro jugador\n 2). Contra la PC\nOpción: ")

jugador = "X"
jugadas = 0
ganador = False

# Ciclo principal del juego
while not ganador and jugadas < 9:
    print("\nTablero actual:")
    print(f"""
 {tablero[0][0]} | {tablero[0][1]} | {tablero[0][2]}
---+---+---
 {tablero[1][0]} | {tablero[1][1]} | {tablero[1][2]}
---+---+---
 {tablero[2][0]} | {tablero[2][1]} | {tablero[2][2]}
""")

    if modo == "2" and jugador == "O": # Elección de casilla
        print("Turno de la PC...")
        casilla = random.randint(1,9)
        fila = (casilla - 1) // 3
        columna = (casilla - 1) % 3
        while tablero[fila][columna] != " ":
            casilla = random.randint(1, 9)
            fila = (casilla - 1) // 3
            columna = (casilla - 1) % 3
        print("La PC eligió la casilla", casilla)
        
    else:
        casilla = input(f"Jugador {jugador}, elige una casilla (1-9): ")
        if not casilla.isdigit():
            print("Debes ingresar un número entre 1 y 9.")
            continue
        casilla = int(casilla)
        if casilla < 1 or casilla > 9:
            print("Casilla no válida. Intenta de nuevo.")
            continue
        fila = (casilla - 1) // 3
        columna = (casilla - 1) % 3
        if tablero[fila][columna] != " ":
            print("Esa casilla ya está ocupada.")
            continue

    tablero[fila][columna] = jugador
    jugadas += 1

    #GANADOR
    celdas = [tablero[i][j] for i in range(3) for j in range(3)]
    for a, b, c in ganadoras:
        if celdas[a] == celdas[b] == celdas[c] != " ":
            ganador = True
            break

    if ganador:
        print(f"\n¡Jugador {jugador} HA GANADO!")
        print(f"""
 {tablero[0][0]} | {tablero[0][1]} | {tablero[0][2]}
---+---+---
 {tablero[1][0]} | {tablero[1][1]} | {tablero[1][2]}
---+---+---
 {tablero[2][0]} | {tablero[2][1]} | {tablero[2][2]}
""")
        break

    #EMPATE
    if jugadas == 9 and not ganador:
        print("\nJuego en empate.")
        print(f"""
 {tablero[0][0]} | {tablero[0][1]} | {tablero[0][2]}
---+---+---
 {tablero[1][0]} | {tablero[1][1]} | {tablero[1][2]}
---+---+---
 {tablero[2][0]} | {tablero[2][1]} | {tablero[2][2]}
""")
        break

    # Cambiar de jugador
    if jugador == "X":
        jugador = "O"
    else:
        jugador = "X"
