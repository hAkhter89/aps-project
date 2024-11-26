import pygame
import auxilfuncs

pygame.init()

screen_width=800
screen_height=800

screen = pygame.display.set_mode([screen_width,screen_height])
pygame.display.set_caption('Two Player Pygame Chess')
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
bp = pygame.transform.scale(pygame.image.load('alpha/bP.png'), (80,80))
wq = pygame.transform.scale(pygame.image.load('alpha/wQ.png'), (80,80))
wk = pygame.transform.scale(pygame.image.load('alpha/wK.png'), (80,80))
wr = pygame.transform.scale(pygame.image.load('alpha/wR.png'), (80,80))
wb = pygame.transform.scale(pygame.image.load('alpha/wB.png'), (80,80))
wn = pygame.transform.scale(pygame.image.load('alpha/wN.png'), (80,80))
wp = pygame.transform.scale(pygame.image.load('alpha/wP.png'), (80,80))

white_imgs = [auxilfuncs.wp, auxilfuncs.wq, auxilfuncs.wk, auxilfuncs.wn, auxilfuncs.wb, auxilfuncs.wr]

black_imgs = [auxilfuncs.bp, auxilfuncs.bq, auxilfuncs.bk, auxilfuncs.bn, auxilfuncs.bb, auxilfuncs.br]

piece_list = ['pawn', 'queen', 'king', 'knight', 'bishop', 'rook']


                
#check variables


#board color

light_brown = (240,219,182)
green = (111,130,56)


#drawing the main board

def draw_board():
    for i in range(32):  #32 because we will use the background fill color for the black squares of the board
        column= i % 4
        row= i // 4
        if row % 2 == 0:
            pygame.draw.rect(screen,green,[600 - (column * 200), row* 100, 100, 100])
        else:
            pygame.draw.rect(screen,green,[700 - (column * 200), row* 100, 100, 100])

def draw_pieces():
    for i in range(len(black_pieces)):
        imgindex = piece_list.index(black_pieces[i])
        if black_pieces[i] == 'pawn':
            screen.blit(bp, (black_coords[i][0] * 100 + 8, black_coords[i][1] * 100 + 18))
        else:
            screen.blit(black_imgs[imgindex], (black_coords[i][0] * 100 + 8, black_coords[i][1] * 100 + 18))
            
    for i in range(len(white_pieces)):
        imgindex = piece_list.index(white_pieces[i])
        if white_pieces[i] == 'pawn':
            screen.blit(wp, (white_coords[i][0] * 100 + 8, white_coords[i][1] * 100 + 18))
        else:
            screen.blit(white_imgs[imgindex], (white_coords[i][0] * 100 + 8, white_coords[i][1] * 100 + 18))    
    
            
        # functions to check all pices valid option
def check_options(pieces, locations, turn):
    moves_list = []
    all_moves_list = []
    for i in range (len(pieces)):
        location = locations[i]
        piece = pieces[i]
        if piece == 'pawn':
            moves_list = check_pawn(location, turn)
        # elif piece == 'rook':
        #     moves_list = check_rook(location, turn)
        # elif piece == 'knight':
        #     moves_list = check_knight(location, turn)
        # elif piece == 'bishop':
        #     moves_list = check_bishop(location, turn)
        # elif piece == 'queen':
        #     moves_list = check_queen(location, turn)
        # elif piece == 'king':
        #     moves_list = check_king(location, turn)
        all_moves_list.append(moves_list)

    return all_moves_list 





    #hassan I'm thinking about making a seperate texture for the board in the wooden style so this is just a placeholder
    # I've removed the discard pile tab, we dont need it. - Hassan

#check valid pon moves
def check_pawn(position, color):
    moves_list = []
    if color == 'white':
        if (position [0], position[1] + 1) not in white_coords and (position [0], position[1] + 1) not in black_coords and position[1] < 7:
            moves_list.append((position[0], position[1] + 1))
        if (position [0], position[1] + 2) not in white_coords and (position [0], position[1] + 2) not in black_coords and position[1] == 1:
            moves_list.append((position[0], position[1] + 2))
        if (position[0] + 1, position [1] + 1) in black_coords:
            moves_list.append((position[0] + 1, position [1] + 1))
        if (position[0] - 1, position [1] + 1) in black_coords:
            moves_list.append((position[0] - 1, position [1] + 1))


    else:
        if (position [0], position[1] - 1) not in white_coords and (position [0], position[1] - 1) not in black_coords and position[1] > 0:
            moves_list.append((position[0], position[1] - 1))
        if (position [0], position[1] - 2) not in white_coords and (position [0], position[1] - 2) not in black_coords and position[1] == 6:
            moves_list.append((position[0], position[1] - 2))
        if (position[0] + 1, position [1] - 1) in white_coords:
            moves_list.append((position[0] + 1, position [1] - 1))
        if (position[0] - 1, position [1] + 1) in white_coords:
            moves_list.append((position[0] - 1, position [1] - 1))
    return moves_list




# check for valid moves for just selected piece
def check_valid_moves():
    if turn_step < 2:
        options_list = white_options
    else:
        options_list = black_options
    valid_options = options_list[selected]
    return valid_options








#draw valid moves on screen
def draw_valid(moves):
    if turn_step < 2:
        color = 'red'
    else:
        color = 'blue'
    for i in range(len(moves)):
        pygame.draw.circle(screen, color, (moves[i][0] * 100 + 50, moves[i][1] *100 + 50),5)





#gameloop
black_options = check_options(black_pieces, black_coords, 'black')
white_options = check_options(white_pieces, white_coords, 'white')

run = True

while run == True:


    timer.tick(fps)
    screen.fill(light_brown)
    draw_board()
    draw_pieces()
    if selected != 100:
        valid_moves = check_valid_moves()
        draw_valid(valid_moves)

#event handelling


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x_coord = event.pos[0] // 100
            y_coord = event.pos[1] // 100
            click_coord = (x_coord, y_coord)
            if turn_step <= 1:
                if click_coord in white_coords:
                    selected = white_coords.index(click_coord)
                    if turn_step == 0:
                        turn_step = 1
                if click_coord in legal_moves and selected != 100:
                    white_coords[selected] = click_coord
                    if click_coord in black_coords:
                        black_piece = black_coords.index(click_coord)
                        capture_white.append(black_pieces[black_piece])
                        black_pieces.pop(black_piece)
                        black_coords.pop(black_piece)
                    black_options = check_options(black_piece, black_coords, 'black')
                    white_options = check_options(white_piece, white_coords, 'white')
                    turn_step = 2
                    selected = 100
                    legal_moves = []
            if turn_step > 1:
                if click_coord in black_coords:
                    selected = black_coords.index(click_coord)
                    if turn_step == 2:
                        turn_step = 3
                    if click_coord in legal_moves and selected != 100:
                        black_coords[selected] = click_coord
                    if click_coord in white_coords:
                        white_piece = white_coords.index(click_coord)
                        capture_black.append(white_pieces[white_piece])
                        white_pieces.pop(white_piece)
                        white_coords.pop(white_piece)
                    black_options = check_options(black_piece, black_coords, 'black')
                    white_options = check_options(white_piece, white_coords, 'white')
                    turn_step = 0
                    selected = 100
                    legal_moves = []



   
   
   
   
   
   
    pygame.display.flip()
   

pygame.quit()
