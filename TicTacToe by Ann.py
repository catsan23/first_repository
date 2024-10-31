import pygame
import sys

# initialize Pygame
pygame.init()

# Set up display
size = width, height = 300, 350  # Window size (adjusted height for the message)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tic Tac Toe")

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Define the board and state
# Initialize an empty board
board = []

# Create a 3x3 grid
for i in range(3):
    row = []  # Create a new row
    for j in range(3):
        row.append("")  # Add an empty string for each cell in the row
    board.append(row)  # Add the row to the board

# The board now looks like this:
# [["", "", ""],
#  ["", "", ""],
#  ["", "", ""]]

# set global variables at the beginning
current_player = "X"
winner = None
game_over = False

# Fonts
font = pygame.font.Font(None, 100)
small_font = pygame.font.Font(None, 50)

def draw_board():
    screen.fill(white)  # Fill the screen with white

    # Draw the grid
    pygame.draw.line(screen, black, (100, 0), (100, 300), 3 ) #horizontal line
    pygame.draw.line(screen, black, (200, 0), (200, 300), 3) #horizontal line
    pygame.draw.line(screen, black, (0, 100), (300, 100), 3) #vertikal
    pygame.draw.line(screen, black, (0, 200), (300, 200), 3) #vertikal

    # Draw the X's and O's: loops through each cell in teh 3x3 grid
    for row in range(3):
        for col in range(3):
            if board[row][col] == "X":
                text = font.render("X", True, black) #creates text
                screen.blit(text, (col * 100 + 25, row * 100 + 15)) #places rendered text on surface
            elif board[row][col] == "O":
                text = font.render("O", True, red)
                screen.blit(text, (col * 100 + 25, row * 100 + 15))


def check_winner():
    global winner #because we want modify winner OUTSIDE the fucntion
    # Check rows and columns
    for i in range(3): #iterate through rows and columns
        if board[i][0] == board[i][1] == board[i][2] != "": #in one row all same symbols?
            winner = board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != "": #in one column all same symbols?
            winner = board[0][i]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != "":
        winner = board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        winner = board[0][2]

def check_draw(): #do we have a draw aka all cells are filled and no winner?
    for row in board:
        if "" in row: #checks for empty cells --> still moves possible
            return False
    return True

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # thats the close button
            pygame.quit()
            sys.exit() #program exits entirely, no need for running = False
        if event.type == pygame.MOUSEBUTTONDOWN and not winner: #if player clicked  mouse button and if no one has won yet
            mouse_x, mouse_y = event.pos
            print(f"Mouse clicked at: ({mouse_x}, {mouse_y})")

            if mouse_y < 300:  # checks that clicks are within the grid
                col = mouse_x // 100
                row = mouse_y // 100

                if board[row][col] == "": #is clicked cell empty?
                    board[row][col] = current_player #updates cell with either X or O
                    check_winner()
                    print(f"Cell selected: row={row}, col={col}")
                    print(f"Current board state: {board}")
                    if winner is None and not check_draw():
                        current_player = "O" if current_player == "X" else "X" #if no winner and board isn’t full: if true, toggle between "X" and "O"
                    elif check_draw() and not winner: #If board full and there’s no winner: draw
                        winner = "Draw"

    draw_board() #called in every loop iteration to refresh  board and display updated state on screen

    if winner:
        result_text = f"Winner: {winner}" if winner != "Draw" else "It's a Draw!"
        text = small_font.render(result_text, True, black)
        # Display message below the grid
        screen.blit(text, (50, 310))
        game_over = True

    pygame.display.flip()

pygame.quit()
