from triqui import drawBoard, getComputerMove, getPlayerMove, inputPlayerLetter, isBoardFull, isWinner, makeMove, playAgain, whoGoesFirst

# 1. Mostrar mensaje de bienvenida
print("████████╗██████╗ ██╗ ██████╗ ██╗   ██╗██╗")
print("╚══██╔══╝██╔══██╗██║██╔═══██╗██║   ██║██║")
print("   ██║   ██████╔╝██║██║   ██║██║   ██║██║")
print("   ██║   ██╔══██╗██║██║▄▄ ██║██║   ██║██║")
print("   ██║   ██║  ██║██║╚██████╔╝╚██████╔╝██║")
print("   ╚═╝   ╚═╝  ╚═╝╚═╝ ╚══▀▀═╝  ╚═════╝ ╚═╝")

turn = whoGoesFirst() # Indica quién tiene el turno para jugar, el usuario o la computadora.
while True:

    # 2. Crear el tablero
    board = [' '] * 10
    # 3. El usuario debe seleccionar la marca
    playerLetter, computerLetter = inputPlayerLetter()
    # 4. Quién va primero el usuario o la computadora?
    print(turn + ' va primero.')
    jugando = True # El juego ha iniciado

    while jugando:
        if turn == 'Usuario': # 5. Turno del usuario

            # a. Mostrar tablero
            drawBoard(board)
            # b. Pedir jugada al usuario
            move = getPlayerMove(board)
            # c. Actualizar el tablero
            makeMove(board, playerLetter, move)

            # d. Verificar si el usuario ha ganado el juego.
            if isWinner(board, playerLetter):
                drawBoard(board)
                print('Melo!, ganaste el juego')
                gameIsPlaying = False
                break
            #    Si si, mostrar tablero, mostrar mensaje de felicitación y terminar el juego.

            # e. Verificar si hay empate.
            else:
                if isBoardFull(board):
                    drawBoard(board)
                    print('Es un empate!')
                    break
            #    Si si, mostrar tablero, mostar mensaje de empate y terminar el juego.

            # f. Si el usuario no ha ganado y no hay empate, la computadora
                else:
                    turn = 'computador'
            #    toma el siguiente turno

            turn = 'Computador'

        else: # 6. Turno de la computadora.

            # a. Computadora hace jugada.
            move = getComputerMove(board, computerLetter)
            # b. Actualizar el tablero.
            makeMove(board, computerLetter, move)
            

            # c. Verificar si la computadora ha ganado el juego.
            if isWinner(board, computerLetter):
                drawBoard(board)
                print('El computador te ha vencido! Eres un perdedor.')
                gameIsPlaying = False
                break
            #    Si si, mostrar tablero, mostrar mensaje indicando al usuario que ha perdido y terminar el juego.

            # d. Verificar si hay empate.
            else:
                if isBoardFull(board):
                    drawBoard(board)
                    print('Es un empate!')
                    break
            #    Si si, mostrar tablero, mostar mensaje de empate y terminar el juego.

            # f. Si la computadora no ha ganado y no hay empate, el usuario
                else:
                    turn = 'Usuario'
            #    toma el siguiente turno.

            turn = 'Usuario'

    # 7. Preguntar si el usuario quiere jugar una vez mas
    
    if not playAgain():
            break
    #    Si no, finalizar el programa.
