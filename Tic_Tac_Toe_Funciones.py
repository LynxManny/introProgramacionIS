import random

def crear_tablero():
    return [[" " for _ in range(3)] for _ in range(3)]

def mostrar_tablero(tablero):
    print(f"""
 {tablero[0][0]} | {tablero[0][1]} | {tablero[0][2]}
---+---+---
 {tablero[1][0]} | {tablero[1][1]} | {tablero[1][2]}
---+---+---
 {tablero[2][0]} | {tablero[2][1]} | {tablero[2][2]}
""")

def casillas_ganadoras():
    return [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

def tablero_lineal(tablero):
    return [tablero[i][j] for i in range(3) for j in range(3)]

def hay_ganador(tablero):
    celdas = tablero_lineal(tablero)
    for a, b, c in casillas_ganadoras():
        if celdas[a] == celdas[b] == celdas[c] != " ":
            return True
    return False

def tablero_lleno(tablero):
    return all(c != " " for c in tablero_lineal(tablero))

def colocar_ficha(tablero, casilla, jugador):
    nuevo = [fila[:] for fila in tablero]  # Copia inmutable
    fila, columna = (casilla - 1) // 3, (casilla - 1) % 3
    nuevo[fila][columna] = jugador
    return nuevo

def casilla_valida(tablero, casilla):
    if casilla < 1 or casilla > 9:
        return False
    fila, columna = (casilla - 1) // 3, (casilla - 1) % 3
    return tablero[fila][columna] == " "

def pedir_casilla(tablero, jugador):
    casilla = input(f"Jugador {jugador}, elige una casilla (1-9): ")
    if not casilla.isdigit():
        print("Debes ingresar un número entre 1 y 9.")
        return pedir_casilla(tablero, jugador)
    casilla = int(casilla)
    if not casilla_valida(tablero, casilla):
        print("Casilla no válida o ya ocupada.")
        return pedir_casilla(tablero, jugador)
    return casilla

def elegir_casilla_pc(tablero):
    casilla = random.randint(1, 9)
    if not casilla_valida(tablero, casilla):
        return elegir_casilla_pc(tablero)
    print("La PC eligió la casilla", casilla)
    return casilla

def cambiar_jugador(jugador):
    return "O" if jugador == "X" else "X"

def jugar(tablero, jugador, modo):
    mostrar_tablero(tablero)

    if hay_ganador(tablero):
        print(f"¡Jugador {cambiar_jugador(jugador)} HA GANADO!")
        return

    if tablero_lleno(tablero):
        print("Juego en empate.")
        return

    if modo == "2" and jugador == "O":
        print("Turno de la PC...")
        casilla = elegir_casilla_pc(tablero)
    else:
        casilla = pedir_casilla(tablero, jugador)

    nuevo_tablero = colocar_ficha(tablero, casilla, jugador)
    jugar(nuevo_tablero, cambiar_jugador(jugador), modo)

#Inicio del juego
print("=== BIENVENIDO AL JUEGO TIC TAC TOE ===\n")
print("Las posiciones del tablero son:")
print("""
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
""")

modo = input("Modo de juego:\n 1). Contra otro jugador\n 2). Contra la PC\nOpción: ")

jugar(crear_tablero(), "X", modo)
