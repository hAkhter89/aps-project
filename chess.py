import pygame

pygame.init()
screen_width=800
screen_height=800

screen = pygame.display.set_mode([screen_width,screen_height])
pygame.display.set_caption('v0.9.1')
font = pygame.font.Font('freesansbold.ttf', 20) 
big_font = pygame.font.Font('freesansbold.ttf', 50)
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


#board color
board_png = pygame.transform.scale(pygame.image.load('alpha/chessboard.png'), (800,800))
light_brown = (240,219,182)
green = (111,130,56)


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
    
            
        # functions to check all pices valid option
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
        if (position[0], position[1] - 1) not in white_coords and \
                (position[0], position[1] - 1) not in black_coords and position[1] > 0:
            moves_list.append((position[0], position[1] - 1))
        if (position[0], position[1] - 2) not in white_coords and \
                (position[0], position[1] - 2) not in black_coords and position[1] == 6:
            moves_list.append((position[0], position[1] - 2))
        if (position[0] + 1, position[1] - 1) in black_coords:
            moves_list.append((position[0] + 1, position[1] - 1))
        if (position[0] - 1, position[1] - 1) in black_coords:
            moves_list.append((position[0] - 1, position[1] - 1))
    else:
        if (position[0], position[1] + 1) not in white_coords and \
                (position[0], position[1] + 1) not in black_coords and position[1] < 7:
            moves_list.append((position[0], position[1] + 1))
        if (position[0], position[1] + 2) not in white_coords and \
                (position[0], position[1] + 2) not in black_coords and position[1] == 1:
            moves_list.append((position[0], position[1] + 2))
        if (position[0] + 1, position[1] + 1) in white_coords:
            moves_list.append((position[0] + 1, position[1] + 1))
        if (position[0] - 1, position[1] + 1) in white_coords:
            moves_list.append((position[0] - 1, position[1] + 1))
    return moves_list

def check_rook(position, color):
    moves_list = []
    flag = True
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

def check_knight(position, color):
    moves_list = []
    if color == 'white':
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

    screen.fill(light_brown)
    draw_board()
    draw_pieces()
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
                if click_coords in white_coords:
                    print({click_coords})
                    selected = white_coords.index(click_coords)
                    if turn_step == 0:
                        turn_step = 1
                if click_coords in legal_moves and selected != 100:
                    print({click_coords})
                    white_coords[selected] = click_coords
                    if click_coords in black_coords:
                        black_piece = black_coords.index(click_coords)
                        capture_black.append(black_pieces[black_piece])
                        black_pieces.pop(black_piece)
                        black_coords.pop(black_piece)
                    black_options = check_options(black_pieces, black_coords, 'black')
                    white_options = check_options(white_pieces, white_coords, 'white')
                    turn_step = 2
                    selected = 100
                    legal_moves = []
            if turn_step > 1:
                if click_coords in black_coords:
                    selected = black_coords.index(click_coords)
                    if turn_step == 2:
                        turn_step = 3
                if click_coords in legal_moves and selected != 100:
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
