from random import randrange

board = [
    [1, 2, 3],
    [4, 'X', 6],
    [7, 8, 9]
]
def display_board(board):
    print("+---+---+---+")
    for row in board:
        print(f"| {row[0]} | {row[1]} | {row[2]} |")
        print("+---+---+---+")

def enter_move(board):
    essai = int(input('À ton tour de jouer, entre un nombre entre 1 et 9 : '))

    while essai < 1 or essai > 9:
        essai = int(input("Erreur : Veuillez entrer un nombre valide entre 1 et 9 : "))

    case_trouvee = False

    for i in range(3):
        for j in range(3):
            if board[i][j] == essai:  
                board[i][j] = 'O'  
                case_trouvee = True  
                break  
        if case_trouvee:  
            break  

    if not case_trouvee:
        print("Case déjà occupée ! Veuillez rejouer.")
        return enter_move(board)

    display_board(board)

def make_list_of_free_fields(board):
    list_free = []  

    for i in range(3):
        for j in range(3):
            if isinstance(board[i][j], int) and 1 <= board[i][j] <= 9:  
                list_free.append((i, j))  

    return list_free  

def victory_for(board, sign):

    for row in board:
        if row == [sign, sign, sign]:  
            print(f"Le joueur '{sign}' a gagné ! ")
            return True  


    for col in range(3):
        if board[0][col] == sign and board[1][col] == sign and board[2][col] == sign:
            print(f"Le joueur '{sign}' a gagné ! ")
            return True  

    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        print(f"Le joueur '{sign}' a gagné ! ")
        return True  

    if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        print(f"Le joueur '{sign}' a gagné ! ")
        return True  

    return False  

def draw_move(board):
    print("Au tour de l'ordinateur...")

    free_spaces = make_list_of_free_fields(board)

    if not free_spaces:
        print("Match nul ! Plus aucune case libre.")
        return  

    i, j = free_spaces[randrange(len(free_spaces))]  
    board[i][j] = 'X'  

    display_board(board)

# === BOUCLE PRINCIPALE DU JEU ===
display_board(board)

while True:
    enter_move(board)
    if victory_for(board, 'O'):  
        break  

    if not make_list_of_free_fields(board):
        print("Match nul ! Aucune case disponible.")
        break  

    draw_move(board)
    if victory_for(board, 'X'):  
        break  

    if not make_list_of_free_fields(board):
        print("Match nul ! Aucune case disponible.")
        break  
