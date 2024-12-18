import pygame

pygame.init()
screen_width=800
screen_height=800

screen = pygame.display.set_mode([screen_width,screen_height])
pygame.display.set_caption('v0.9.9 - 2 player chess (Ayaan, Hassan, Mustafeez)')
timer = pygame.time.Clock()
fps = 60

#textures and gameloop

white_pieces = ['rook','knight','bishop','king','queen','bishop','knight','rook',
                'pawn','pawn','pawn','pawn','pawn','pawn','pawn','pawn']
black_pieces = ['rook','knight','bishop','king','queen','bishop','knight','rook',
                'pawn','pawn','pawn','pawn','pawn','pawn','pawn','pawn']
black_coords = [(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),
                (0,1),(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1)]

white_coords = [(0,7),(1,7),(2,7),(3,7),(4,7),(5,7),(6,7),(7,7),
                (0,6),(1,6),(2,6),(3,6),(4,6),(5,6),(6,6),(7,6)]



capture_white = []
capture_black = []

#turns


turn_step = 0
selected = 100

legal_moves = []

#textures and assets
bq = pygame.transform.scale(pygame.image.load('alpha/bQ.png'), (80,80))
bk = pygame.transform.scale(pygame.image.load('alpha/bK.png'), (80,80))
br = pygame.transform.scale(pygame.image.load('alpha/bR.png'), (80,80))
bb = pygame.transform.scale(pygame.image.load('alpha/bB.png'), (80,80))
bn = pygame.transform.scale(pygame.image.load('alpha/bN.png'), (80,80))
bp = pygame.transform.scale(pygame.image.load('alpha/bP.png'), (75,75))
wq = pygame.transform.scale(pygame.image.load('alpha/wQ.png'), (80,80))
wk = pygame.transform.scale(pygame.image.load('alpha/wK.png'), (80,80))
wr = pygame.transform.scale(pygame.image.load('alpha/wR.png'), (80,80))
wb = pygame.transform.scale(pygame.image.load('alpha/wB.png'), (80,80))
wn = pygame.transform.scale(pygame.image.load('alpha/wN.png'), (80,80))
wp = pygame.transform.scale(pygame.image.load('alpha/wP.png'), (75,75))

white_imgs = [wp, wq, wk, wn, wb, wr]

black_imgs = [bp, bq, bk, bn, bb, br]

piece_list = ['pawn', 'queen', 'king', 'knight', 'bishop', 'rook']


                
#check variables
white_can_castle = True
black_can_castle = True


#board color
board_png = pygame.transform.scale(pygame.image.load('alpha/chessboard.png'), (800,800))
light_brown = (1,1,1)
brown = (1,1,1)


#Flashing Counter:

counter = 0



def draw_board():
    screen.blit(board_png,(0,0))

def draw_pieces():
    for i in range(len(black_pieces)):
        imgindex = piece_list.index(black_pieces[i])
        if black_pieces[i] == 'pawn':
            screen.blit(bp, (black_coords[i][0] * 100 + 10, black_coords[i][1] * 100 + 20))
        else:
            screen.blit(black_imgs[imgindex], (black_coords[i][0] * 100 + 8, black_coords[i][1] * 100 + 18))
            
    for i in range(len(white_pieces)):
        imgindex = piece_list.index(white_pieces[i])
        if white_pieces[i] == 'pawn':
            screen.blit(wp, (white_coords[i][0] * 100 + 10, white_coords[i][1] * 100 + 20))
        else:
            screen.blit(white_imgs[imgindex], (white_coords[i][0] * 100 + 8, white_coords[i][1] * 100 + 18))    
    
            
# functions to check all pices valid option, this returns a NESTED LIST of all valid moves(tuples) in a turn, later the piecewise valid moves can be indexed by doing all_moves_list[selected]
def check_options(pieces, locations, turn):
    moves_list = []
    all_moves_list = []
    for i in range((len(pieces))):
        location = locations[i]
        piece = pieces[i]
        if piece == 'pawn':
            moves_list = check_pawn(location, turn)
        elif piece == 'rook':
            moves_list = check_rook(location, turn)
        elif piece == 'knight':
            moves_list = check_knight(location, turn)
        elif piece == 'bishop':
            moves_list = check_bishop(location, turn)
        elif piece == 'queen':
            moves_list = check_queen(location, turn)
        elif piece == 'king':
            moves_list = check_king(location, turn)
        all_moves_list.append(moves_list)
    return all_moves_list

def check_pawn(position, color):
    moves_list = []
    if color == 'white':
        # checks if y coordinate - 1 (up the board) is occupied by either white piece of black piece, if not its a valid move
        if (position[0], position[1] - 1) not in white_coords and \
                (position[0], position[1] - 1) not in black_coords and position[1] > 0:
            moves_list.append((position[0], position[1] - 1))
        if (position[0], position[1] - 2) not in white_coords and \
                (position[0], position[1] - 2) not in black_coords and position[1] == 6:
            moves_list.append((position[0], position[1] - 2))
    # Checks if theres a an opposing piece to the diagnol of current square. if so, its a valid move
        if (position[0] + 1, position[1] - 1) in black_coords:
            moves_list.append((position[0] + 1, position[1] - 1))
        if (position[0] - 1, position[1] - 1) in black_coords:
            moves_list.append((position[0] - 1, position[1] - 1))
    else:
        # checks if y coordinate + 1 (down the board) is occupied by either white piece of black piece, if not its a valid move
        if (position[0], position[1] + 1) not in white_coords and \
                (position[0], position[1] + 1) not in black_coords and position[1] < 7:
            moves_list.append((position[0], position[1] + 1))
        if (position[0], position[1] + 2) not in white_coords and \
                (position[0], position[1] + 2) not in black_coords and position[1] == 1:
            moves_list.append((position[0], position[1] + 2))
    # Checks if theeres an opposing peice to the diagnol of the curretn square, if so its a valid move
        if (position[0] + 1, position[1] + 1) in white_coords:
            moves_list.append((position[0] + 1, position[1] + 1))
        if (position[0] - 1, position[1] + 1) in white_coords:
            moves_list.append((position[0] - 1, position[1] + 1))
    return moves_list

def check_rook(position, color):
    moves_list = []
    flag = True
    if color == 'white':
        # UP Loops to check if each square is not occupied by a piece, if it is the loop breaks and the valid moves are appended as the rook cannot see through pieces
        for x in range(1, position[1] + 1):
            if (position[0], position[1] - x) not in white_coords:
                if (position[0], position[1] - x) in black_coords:
                    moves_list.append((position[0], position[1] - x))
                    break
                else:
                    moves_list.append((position[0], position[1] - x))
            else:
                break
        # DOWN Loops to check if each square is not occupied by a piece if it is the loops are broken, and valid moves uptill that point are appended to moveslist
        for x in range(1, abs(position[1] - 7) + 1):
            if (position[0], position[1] + x) not in white_coords:
                if (position[0], position[1] + x) in black_coords:
                    moves_list.append((position[0], position[1] + x))
                    break
                else:
                    moves_list.append((position[0], position[1] + x))
            else:
                break
        # LEFT ///
        for x in range(1, position[0] + 1):
            if (position[0] - x, position[1]) not in white_coords:
                if (position[0] - x, position[1]) in black_coords:
                    moves_list.append((position[0] - x, position[1]))
                    break
                else:
                    moves_list.append((position[0] - x, position[1]))
            else:
                break
        # RIGHT ////
        for x in range(1, abs(position[0] - 7) + 1):
            if (position[0] + x, position[1]) not in white_coords:
                if (position[0] + x, position[1]) in black_coords:
                    moves_list.append((position[0] + x, position[1]))
                    break
                else:
                    moves_list.append((position[0] + x, position[1]))
            else:
                break
    else:
        # UP
        for x in range(1, abs(position[1] - 7) + 1):
            if (position[0], position[1] + x) not in black_coords:
                if (position[0], position[1] + x) in white_coords:
                    moves_list.append((position[0], position[1] + x))
                    break
                else:
                    moves_list.append((position[0], position[1] + x))
            else:
                break
        # DOWN
        for x in range(1, position[1] + 1):
            if (position[0], position[1] - x) not in black_coords:
                if (position[0], position[1] - x) in white_coords:
                    moves_list.append((position[0], position[1] - x))
                    break
                else:
                    moves_list.append((position[0], position[1] - x))
            else:
                break
        # LEFT
        for x in range(1, abs(position[0] - 7) + 1):
            if (position[0] + x, position[1]) not in black_coords:
                if (position[0] + x, position[1]) in white_coords:
                    moves_list.append((position[0] + x, position[1]))
                    break
                else:
                    moves_list.append((position[0] + x, position[1]))
            else:
                break
        # RIGHT
        for x in range(1, position[0] + 1):
            if (position[0] - x, position[1]) not in black_coords:
                if (position[0] - x, position[1]) in white_coords:
                    moves_list.append((position[0] - x, position[1]))
                    break
                else:
                    moves_list.append((position[0] - x, position[1]))
            else:
                break
    return moves_list

def check_knight(position, color):
    moves_list = []
    if color == 'white':
    # The knight moves in an L shape, i.e 2 square in the y coordinate and 1 in the x coordinate. Total 8 possible moves sometimes the combination will also be 2 square in the x coordinate and 1 in the y coordinate, same for black.
        if (position[0] + 1, position[1] - 2) not in white_coords:
            moves_list.append((position[0] + 1, position[1] - 2))
        if (position[0] - 1, position[1] - 2) not in white_coords:
            moves_list.append((position[0] - 1, position[1] - 2))
            
        if (position[0] - 1, position[1] + 2) not in white_coords:
            moves_list.append((position[0] - 1, position[1] + 2))
        if (position[0] + 1, position[1] + 2) not in white_coords:
            moves_list.append((position[0] + 1, position[1] + 2))
            
        if (position[0] - 2, position[1] - 1) not in white_coords:
            moves_list.append((position[0] - 2, position[1] - 1))
        if (position[0] - 2, position[1] + 1) not in white_coords:
            moves_list.append((position[0] - 2, position[1] + 1))
            
        if (position[0] + 2, position[1] - 1) not in white_coords:
            moves_list.append((position[0] + 2, position[1] - 1))
        if (position[0] + 2, position[1] + 1) not in white_coords:
            moves_list.append((position[0] + 2, position[1] + 1))
    else:
        if (position[0] + 1, position[1] - 2) not in black_coords:
            moves_list.append((position[0] + 1, position[1] - 2))
        if (position[0] - 1, position[1] - 2) not in black_coords:
            moves_list.append((position[0] - 1, position[1] - 2))
            
        if (position[0] - 1, position[1] + 2) not in black_coords:
            moves_list.append((position[0] - 1, position[1] + 2))
        if (position[0] + 1, position[1] + 2) not in black_coords:
            moves_list.append((position[0] + 1, position[1] + 2))
            
        if (position[0] - 2, position[1] - 1) not in black_coords:
            moves_list.append((position[0] - 2, position[1] - 1))
        if (position[0] - 2, position[1] + 1) not in black_coords:
            moves_list.append((position[0] - 2, position[1] + 1))
            
        if (position[0] + 2, position[1] - 1) not in black_coords:
            moves_list.append((position[0] + 2, position[1] - 1))
        if (position[0] + 2, position[1] + 1) not in black_coords:
            moves_list.append((position[0] + 2, position[1] + 1))
        
    
    return moves_list

def check_bishop(position, color):
    moves_list = []
    # if the current x sqare is 5 then the moves to the left will be x in range(1, 5 + 1) and moves to the right of the 5 squares will also need to be considered separetly, i.e x in range(1, abs(5-7(7 is the total board lenght) + 1))
    # all the moves are made diaganoly hence x coordinate + 1, y coordinate - 1 and these combinations, this will also be done for diagnol moves in the other 2 directions i.e top down, so if y coord is 5, x in range(1, 5 + 1)..., we're not concernced with their being more moves then squares becuase the board is lociked at 800x800
    if color == 'white':
        # TOP LEFT
        for x in range(1, position[0] + 1):
            if (position[0] - x, position[1] - x) not in white_coords:
                if (position[0] - x, position[1] - x) in black_coords:
                    moves_list.append((position[0] - x, position[1] - x))
                    break
                else:
                    moves_list.append((position[0] - x, position[1] - x))
            else:
                break
        # DOWN RIGHT
        for x in range(1, abs(position[0] - 7) + 1):
            if (position[0] + x, position[1] + x) not in white_coords:
                if (position[0] + x, position[1] + x) in black_coords:
                    moves_list.append((position[0] + x, position[1] + x))
                    break
                else:
                    moves_list.append((position[0] + x, position[1] + x))
            else:
                break
        # DOWN LEFT
        for x in range(1, position[0] + 1):
            if (position[0] - x, position[1] + x) not in white_coords:
                if (position[0] - x, position[1] + x) in black_coords:
                    moves_list.append((position[0] - x, position[1] + x))
                    break
                else:
                    moves_list.append((position[0] - x, position[1] + x))
            else:
                break
        #  UP RIGHT
        for x in range(1, abs(position[0] - 7) + 1):
            if (position[0] + x, position[1] - x) not in white_coords:
                if (position[0] + x, position[1] - x) in black_coords:
                    moves_list.append((position[0] + x, position[1] - x))
                    break
                else:
                    moves_list.append((position[0] + x, position[1] - x))
            else:
                break
    else:
        # FOR BLACK
        for x in range(1, abs(position[0] - 7) + 1):
            if (position[0] + x, position[1] + x) not in black_coords:
                if (position[0] + x, position[1] + x) in white_coords:
                    moves_list.append((position[0] + x, position[1] + x))
                    break
                else:
                    moves_list.append((position[0] + x, position[1] + x))
            else:
                break
        for x in range(1, position[0]  + 1):
            if (position[0] - x, position[1] - x) not in black_coords:
                if (position[0] - x, position[1] - x) in white_coords:
                    moves_list.append((position[0] - x, position[1] - x))
                    break
                else:
                    moves_list.append((position[0] - x, position[1] - x))
            else:
                break
        for x in range(1, abs(position[0] - 7) + 1):
            if (position[0] + x, position[1] - x) not in black_coords:
                if (position[0] + x, position[1] - x) in white_coords:
                    moves_list.append((position[0] + x, position[1] - x))
                    break
                else:
                    moves_list.append((position[0] + x, position[1] - x))
            else:
                break
        for x in range(1, position[0] + 1):
            if (position[0] - x, position[1] + x) not in black_coords:
                if (position[0] - x, position[1] + x) in white_coords:
                    moves_list.append((position[0] - x, position[1] + x))
                    break
                else:
                    moves_list.append((position[0] - x, position[1] + x))
            else:
                break
    return moves_list

def check_queen(position, color):
    # ROOK + BISHOP
    moves_list = []
    if color == 'white':
        for x in range(1, position[0] + 1):
            if (position[0] - x, position[1] - x) not in white_coords:
                if (position[0] - x, position[1] - x) in black_coords:
                    moves_list.append((position[0] - x, position[1] - x))
                    break
                else:
                    moves_list.append((position[0] - x, position[1] - x))
            else:
                break
        for x in range(1, abs(position[0] - 7) + 1):
            if (position[0] + x, position[1] + x) not in white_coords:
                if (position[0] + x, position[1] + x) in black_coords:
                    moves_list.append((position[0] + x, position[1] + x))
                    break
                else:
                    moves_list.append((position[0] + x, position[1] + x))
            else:
                break
        for x in range(1, position[0] + 1):
            if (position[0] - x, position[1] + x) not in white_coords:
                if (position[0] - x, position[1] + x) in black_coords:
                    moves_list.append((position[0] - x, position[1] + x))
                    break
                else:
                    moves_list.append((position[0] - x, position[1] + x))
            else:
                break
        for x in range(1, abs(position[0] - 7) + 1):
            if (position[0] + x, position[1] - x) not in white_coords:
                if (position[0] + x, position[1] - x) in black_coords:
                    moves_list.append((position[0] + x, position[1] - x))
                    break
                else:
                    moves_list.append((position[0] + x, position[1] - x))
            else:
                break
    else:
        for x in range(1, abs(position[0] - 7) + 1):
            if (position[0] + x, position[1] + x) not in black_coords:
                if (position[0] + x, position[1] + x) in white_coords:
                    moves_list.append((position[0] + x, position[1] + x))
                    break
                else:
                    moves_list.append((position[0] + x, position[1] + x))
            else:
                break
        for x in range(1, position[0]  + 1):
            if (position[0] - x, position[1] - x) not in black_coords:
                if (position[0] - x, position[1] - x) in white_coords:
                    moves_list.append((position[0] - x, position[1] - x))
                    break
                else:
                    moves_list.append((position[0] - x, position[1] - x))
            else:
                break
        for x in range(1, abs(position[0] - 7) + 1):
            if (position[0] + x, position[1] - x) not in black_coords:
                if (position[0] + x, position[1] - x) in white_coords:
                    moves_list.append((position[0] + x, position[1] - x))
                    break
                else:
                    moves_list.append((position[0] + x, position[1] - x))
            else:
                break
        for x in range(1, position[0] + 1):
            if (position[0] - x, position[1] + x) not in black_coords:
                if (position[0] - x, position[1] + x) in white_coords:
                    moves_list.append((position[0] - x, position[1] + x))
                    break
                else:
                    moves_list.append((position[0] - x, position[1] + x))
            else:
                break
    if color == 'white':
        # UP
        for x in range(1, position[1] + 1):
            if (position[0], position[1] - x) not in white_coords:
                if (position[0], position[1] - x) in black_coords:
                    moves_list.append((position[0], position[1] - x))
                    break
                else:
                    moves_list.append((position[0], position[1] - x))
            else:
                break
        # DOWN
        for x in range(1, abs(position[1] - 7) + 1):
            if (position[0], position[1] + x) not in white_coords:
                if (position[0], position[1] + x) in black_coords:
                    moves_list.append((position[0], position[1] + x))
                    break
                else:
                    moves_list.append((position[0], position[1] + x))
            else:
                break
        # LEFT
        for x in range(1, position[0] + 1):
            if (position[0] - x, position[1]) not in white_coords:
                if (position[0] - x, position[1]) in black_coords:
                    moves_list.append((position[0] - x, position[1]))
                    break
                else:
                    moves_list.append((position[0] - x, position[1]))
            else:
                break
        # RIGHT
        for x in range(1, abs(position[0] - 7) + 1):
            if (position[0] + x, position[1]) not in white_coords:
                if (position[0] + x, position[1]) in black_coords:
                    moves_list.append((position[0] + x, position[1]))
                    break
                else:
                    moves_list.append((position[0] + x, position[1]))
            else:
                break
    else:
        # UP
        for x in range(1, abs(position[1] - 7) + 1):
            if (position[0], position[1] + x) not in black_coords:
                if (position[0], position[1] + x) in white_coords:
                    moves_list.append((position[0], position[1] + x))
                    break
                else:
                    moves_list.append((position[0], position[1] + x))
            else:
                break
        # DOWN
        for x in range(1, position[1] + 1):
            if (position[0], position[1] - x) not in black_coords:
                if (position[0], position[1] - x) in white_coords:
                    moves_list.append((position[0], position[1] - x))
                    break
                else:
                    moves_list.append((position[0], position[1] - x))
            else:
                break
        # LEFT
        for x in range(1, abs(position[0] - 7) + 1):
            if (position[0] + x, position[1]) not in black_coords:
                if (position[0] + x, position[1]) in white_coords:
                    moves_list.append((position[0] + x, position[1]))
                    break
                else:
                    moves_list.append((position[0] + x, position[1]))
            else:
                break
        # RIGHT
        for x in range(1, position[0] + 1):
            if (position[0] - x, position[1]) not in black_coords:
                if (position[0] - x, position[1]) in white_coords:
                    moves_list.append((position[0] - x, position[1]))
                    break
                else:
                    moves_list.append((position[0] - x, position[1]))
            else:
                break
    return moves_list

def check_king(position, color):
    # 1 square in all directions
    moves_list = []
    if color == 'white':
        if (position[0], position[1] - 1) not in white_coords:
            moves_list.append((position[0], position[1] - 1))
        if (position[0], position[1] + 1) not in white_coords:
            moves_list.append((position[0], position[1] + 1))
        if (position[0] - 1, position[1] - 1) not in white_coords:
            moves_list.append((position[0] - 1, position[1] - 1))
        if (position[0] + 1, position[1] - 1) not in white_coords:
            moves_list.append((position[0] + 1, position[1] - 1))
        if (position[0] - 1, position[1] + 1) not in white_coords:
            moves_list.append((position[0] - 1, position[1] + 1))
        if (position[0] + 1, position[1] + 1) not in white_coords:
            moves_list.append((position[0] + 1, position[1] + 1))
        if (position[0] - 1, position[1]) not in white_coords:
            moves_list.append((position[0] - 1, position[1]))
        if (position[0] + 1, position[1]) not in white_coords:
            moves_list.append((position[0] + 1, position[1]))
    else:
        if (position[0], position[1] - 1) not in black_coords:
            moves_list.append((position[0], position[1] - 1))
        if (position[0], position[1] + 1) not in black_coords:
            moves_list.append((position[0], position[1] + 1))
        if (position[0] - 1, position[1] - 1) not in black_coords:
            moves_list.append((position[0] - 1, position[1] - 1))
        if (position[0] + 1, position[1] - 1) not in black_coords:
            moves_list.append((position[0] + 1, position[1] - 1))
        if (position[0] - 1, position[1] + 1) not in black_coords:
            moves_list.append((position[0] - 1, position[1] + 1))
        if (position[0] + 1, position[1] + 1) not in black_coords:
            moves_list.append((position[0] + 1, position[1] + 1))
        if (position[0] - 1, position[1]) not in black_coords:
            moves_list.append((position[0] - 1, position[1]))
        if (position[0] + 1, position[1]) not in black_coords:
            moves_list.append((position[0] + 1, position[1]))
    # the special castling move in Kingside(O-O) and Queenside(O-O-O) directions
    # KINGSIDE CASTLE O-O    
    if color == 'white' and white_can_castle == True:
        castle_flag = False
        for x in range(1, 3):
            if (position[0] - x, position[1]) not in white_coords and (position[0] - x, position[1]) not in black_coords:
                castle_flag = True
            else: 
                castle_flag = False
                break
        if castle_flag == True:
            moves_list.append((position[0] - 2, position[1]))
    elif color == 'black' and black_can_castle == True:
        castle_flag = False
        for x in range(1, 3):
            if (position[0] - x, position[1]) not in white_coords and (position[0] - x, position[1]) not in black_coords:
                castle_flag = True
            else: 
                castle_flag = False
                break
        if castle_flag == True:
            moves_list.append((position[0] - 2, position[1]))
    # QUEENSIDE CASTLE O-O-O
    if color == 'white' and white_can_castle == True:
        castle_flag = False
        for x in range(1, 4):
            if (position[0] + x, position[1]) not in white_coords and (position[0] + x, position[1]) not in black_coords:
                castle_flag = True
            else: 
                castle_flag = False
                break
        if castle_flag == True:
            moves_list.append((position[0] + 2, position[1]))
    elif color == 'black' and black_can_castle == True:
        castle_flag = False
        for x in range(1, 4):
            if (position[0] + x, position[1]) not in white_coords and (position[0] + x, position[1]) not in black_coords:
                castle_flag = True
            else: 
                castle_flag = False
                break
        if castle_flag == True:
            moves_list.append((position[0] + 2, position[1]))
                
    return moves_list

        
               
    

def check_valid_moves():
    if turn_step < 2:
        options_list = white_options
    else:
        options_list = black_options
    valid_options = options_list[selected]
    return valid_options


#flashing square around king if king in check, if king is capture==checkmate and game over:

def draw_check():
    if turn_step<2: #this means it is the white player's turn
        king_index= white_pieces.index("king")
        king_location=white_coords[king_index]
        for i in range (len(black_options)):
            if king_location in black_options[i]:
                if counter<15: #so that the rectangle flashes every half second
                    pygame.draw.rect(screen,'dark red', [white_coords[king_index][0]*100+1, white_coords[king_index][1]*100+1,100,100],5)

    else: #this means it is the black player's turn
        king_index= black_pieces.index("king")
        king_location=black_coords[king_index]
        for i in range (len(white_options)):
            if king_location in white_options[i]:
                if counter<15: #so that the rectangle flashes every half second
                    pygame.draw.rect(screen,'dark blue', [black_coords[king_index][0]*100+1,black_coords[king_index][1]*100+1,100,100],5)





#gameloop


run = True

while run == True:
    black_options = check_options(black_pieces, black_coords, 'black')
    white_options = check_options(white_pieces, white_coords, 'white')


    timer.tick(fps)

    if counter<30:
        counter+=1
    else:
        counter=0
    draw_board()
    draw_pieces()
    
    if 'king' not in white_pieces:
        print('Checkmate, Black Wins')
        run = False
    elif 'king' not in black_pieces:
        print('Checkmate, White wins')
        run = False
    else:
        draw_check()
    
    if selected != 100:
        legal_moves = check_valid_moves()
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x_coord = event.pos[0] // 100
            y_coord = event.pos[1] // 100   
            click_coords = (x_coord, y_coord)
            
            if turn_step < 2:
                # WHITE'S TURN
                if click_coords in white_coords:
                    # Selected index in the white coords list
                    selected = white_coords.index(click_coords) 
                    if turn_step == 0: 
                        # step = 1 means that a white piece is selected, and thus after a reloop it detects the move-click
                        turn_step = 1
                if selected != 100 and white_pieces[selected] == 'king':
                    # Logic for Castles
                    if click_coords == (1, 7) and click_coords in legal_moves and white_can_castle == True:
                        white_coords[0] = (2,7)
                        white_can_castle = False
                    # Logic for Queenside castles
                    elif click_coords == (5,7) and click_coords in legal_moves and white_can_castle == True:
                        for x in range(1, len(white_pieces[1:])):
                            if white_pieces[x] == 'rook':
                                white_coords[x] = (4,7)
                                white_can_castle = False
                #  At turn = 1 i.e white piece selected, if new click in legal moves then play that move
                if click_coords in legal_moves and selected != 100:
                    white_coords[selected] = click_coords
                    print(f'White plays {click_coords}')
                    if click_coords in black_coords:
                        # if legal move square occupied by opposing peice, means that piece has now been captured therefore remove its entry and coords
                        black_piece = black_coords.index(click_coords)
                        capture_black.append(black_pieces[black_piece])
                        black_pieces.pop(black_piece)
                        black_coords.pop(black_piece)
                    #  recalculate new moves_list from after capture of pieces
                    black_options = check_options(black_pieces, black_coords, 'black')
                    white_options = check_options(white_pieces, white_coords, 'white')
                    turn_step = 2
                    # Turn step 2 = switch turn to black turn after white has played a move and reset selction and legal_moves
                    selected = 100
                    # legal moves are re-calculated every turn
                    legal_moves = []
            if turn_step > 1:
                # Black TURN // same as white turn but replaced all values of white references with black references
                if click_coords in black_coords:
                    selected = black_coords.index(click_coords)
                    if turn_step == 2:
                        turn_step = 3
                if selected != 100  and black_pieces[selected] == 'king':
                    if click_coords == (1, 0) and click_coords in legal_moves and black_can_castle == True:
                        black_coords[0] = (2,0)
                        black_can_castle = False
                    elif click_coords == (5, 0) and click_coords in legal_moves and black_can_castle == True:
                        for x in range(1, len(black_pieces[1:])):
                            if black_pieces[x] == 'rook':
                                black_coords[x] = (4, 0)
                                black_can_castle = False
                if click_coords in legal_moves and selected != 100:
                    print(f'Black plays {click_coords}')
                    black_coords[selected] = click_coords
                    if click_coords in white_coords:
                        white_piece = white_coords.index(click_coords)
                        capture_white.append(white_pieces[white_piece])
                        white_pieces.pop(white_piece)
                        white_coords.pop(white_piece)
                    black_options = check_options(black_pieces, black_coords, 'black')
                    white_options = check_options(white_pieces, white_coords, 'white')
                    turn_step = 0
                    selected = 100
                    legal_moves = []
                        
                
   
   
    pygame.display.flip()
   

pygame.quit()
