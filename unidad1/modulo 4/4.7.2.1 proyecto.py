'''
nombre: José Manuel Gutiérrez Pérez
fecha: 9 de octubre del 2023
Escenario
Tu tarea es escribir un simple programa que simule jugar a tic-tac-toe (nombre en inglés) con el usuario. Para hacerlo más fácil, hemos decidido simplificar el juego. Aquí están nuestras reglas:
La maquina (por ejemplo, el programa) jugará utilizando las 'X's.
El usuario (por ejemplo, tu) jugarás utilizando las 'O's.
El primer movimiento es de la maquina: siempre coloca una 'X' en el centro del tablero.
Todos los cuadros están numerados comenzando con el 1 (observa el ejemplo para que tengas una referencia).
El usuario ingresa su movimiento introduciendo el número de cuadro elegido. El número debe de ser valido, por ejemplo un valor entero mayor que 0 y menor que 10, y no puede ser un cuadro que ya esté ocupado.
El programa verifica si el juego ha terminado. Existen cuatro posibles veredictos: el juego continua, el juego termina en empate, tu ganas, o la maquina gana.
La maquina responde con su movimiento y se verifica el estado del juego.
No se debe implementar algún tipo de inteligencia artificial, la maquina elegirá un cuadro de manera aleatoria, eso es suficiente para este juego.
'''

import random

# Inicializar el tablero
def initialize_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

# Función para imprimir el tablero
def display_board(board):
    print("+---+---+---+")
    for row in board:
        print("| {} | {} | {} |".format(row[0], row[1], row[2]))
        print("+---+---+---+")

# Función para realizar el movimiento del usuario
def enter_move(board):
    while True:
        try:
            move = int(input("Ingresa tu movimiento (1-9): "))
            if 1 <= move <= 9:
                row, col = (move - 1) // 3, (move - 1) % 3
                if board[row][col] == ' ':
                    board[row][col] = 'O'
                    return
                else:
                    print("Cuadro ocupado. Inténtalo de nuevo.")
            else:
                print("Movimiento no válido. Inténtalo de nuevo.")
        except ValueError:
            print("Entrada no válida. Ingresa un número del 1 al 9.")

# Función para construir una lista de cuadros libres
def make_list_of_free_fields(board):
    free_fields = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                free_fields.append((i, j))
    return free_fields

# Función para verificar la victoria
def victory_for(board, sign):
    # Verificar filas y columnas
    for i in range(3):
        if all(board[i][j] == sign for j in range(3)) or all(board[j][i] == sign for j in range(3)):
            return True

    # Verificar diagonales
    if all(board[i][i] == sign for i in range(3)) or all(board[i][2 - i] == sign for i in range(3)):
        return True

    return False

# Función para realizar el movimiento de la máquina
def draw_move(board):
    free_fields = make_list_of_free_fields(board)
    if free_fields:
        row, col = random.choice(free_fields)
        board[row][col] = 'X'

# Juego principal
def main():
    board = initialize_board()
    board[1][1] = 'X'  # Movimiento inicial de la máquina en el centro
    display_board(board)

    while True:
        enter_move(board)
        display_board(board)
        if victory_for(board, 'O'):
            print("¡Has Ganado!")
            break
        free_fields = make_list_of_free_fields(board)
        if not free_fields:
            print("¡Empate!")
            break

        draw_move(board)
        display_board(board)
        if victory_for(board, 'X'):
            print("¡La Máquina ha Ganado!")
            break
        free_fields = make_list_of_free_fields(board)
        if not free_fields:
            print("¡Empate!")
            break

if __name__ == "__main__":
    main()
