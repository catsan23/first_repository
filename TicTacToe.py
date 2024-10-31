import pygame
import sys

#initialize Pygame
pygame.init()

# Set up display size and colors
size = (width, height) = (300, 400)  # Height includes space for messages, increase if you like
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tic Tac Toe") #adjust the title

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Initialize the game board (3x3 grid)
board = [] # Initialize an empty board

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

#global variables to keep track of the game state
current_player = "X"
winner = None
game_over= False 

# Define the fonts for text
font = pygame.font.Font(None, 100)
small_font = pygame.font.Font(None, 50)

def draw_board():
    screen.fill(white)
    # Fill the screen with white
    # Draw grid lines
    for i in range(1,3):
        pygame.draw.line(screen,black, (0,i*100), (300, i*100), 5)
        pygame.draw.line( screen, black, (i*100,0), (i*100,300),5)
        
    # Draw the X and O marks based on the board state
    for row in range(3):
        for col in range(3):
            if board[row][col] == "X":
                text = font.render("X", True, black)
                screen.blit(text, (col* 100+30, row * 100+10))
            elif board [row][col] == "O":
                text = font.render("O", True, red)
                screen.blit(text, (col*100+30, row * 100+10))
    if winner:
        message= small_font.render(f"{winner} wins", True, black)
        screen.blit(message,(10,310))
    elif game_over:
        message= small_font.render("Game over", True, black)
        screen.blit(message,(10,310))
def check_winner():
    global winner, game_over
    # Check rows for a winner
    for i in range(3):
        if board [i][0]== board[i][1]== board [i][2] != "":
            winner =board[i][0]
            game_over= True 
        if board [0][i]== board[1][i]== board [2][i] != "":
            winner =board[0][1]
            game_over= True     
    if board [0][0]== board[1][1]== board [2][2] != "":
        winner =board[0][0]
        game_over= True 
    if board [0][2]== board[1][1]== board [2][0] != "":
        winner =board[0][2]
        game_over= True 
    # Check columns for a winner
    # Check diagonals for a winner
    #return None

def check_draw():
    global game_over
    # Return True if all cells are filled with no winner
    # Return False otherwise
    if all (board[row][col] != "" for row in range(3) for col in range(3)) and not winner:
        game_over= True
    #return None

# Main game loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouse_x, mouse_y =pygame.mouse.get_pos()
            row= mouse_y // 100
            col= mouse_x // 100
            if board [row][col]== "":

           
                board[row][col] = current_player
                check_winner()
                check_draw()
                 #if not game_over:
                current_player ="O" if current_player == "X" else "X"
            print(f"Mouse clicked at: ({mouse_x}, {mouse_y})")
            print(f"Cell selected: row={row}, col={col}")
            print(f"Current board state: {board}")

    draw_board()  # Update the grid
    # Display winner message if game is over
    pygame.display.flip()  # Refresh the display


# Exit Pygame properly
pygame.quit()
