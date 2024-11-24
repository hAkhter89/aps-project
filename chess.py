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
bq_small = pygame.transform.scale(bq, (45,45))
bk = pygame.transform.scale(pygame.image.load('alpha/bK.png'), (80,80))
bk_small = pygame.transform.scale(bk, (45,45))
br = pygame.transform.scale(pygame.image.load('alpha/bR.png'), (80,80))
br_small = pygame.transform.scale(br, (45,45))
bb = pygame.transform.scale(pygame.image.load('alpha/bB.png'), (80,80))
bb_small = pygame.transform.scale(bb, (45,45))
bn = pygame.transform.scale(pygame.image.load('alpha/bN.png'), (80,80))
bn_small = pygame.transform.scale(bn, (45,45))
bp = pygame.transform.scale(pygame.image.load('alpha/bP.png'), (80,80))
bp_small = pygame.transform.scale(bp, (45,45))
wq = pygame.transform.scale(pygame.image.load('alpha/wQ.png'), (80,80))
wq_small = pygame.transform.scale(wq, (45,45))
wk = pygame.transform.scale(pygame.image.load('alpha/wK.png'), (80,80))
wk_small = pygame.transform.scale(wk, (45,45))
wr = pygame.transform.scale(pygame.image.load('alpha/wR.png'), (80,80))
wr_small = pygame.transform.scale(wr, (45,45))
wb = pygame.transform.scale(pygame.image.load('alpha/wB.png'), (80,80))
wb_small = pygame.transform.scale(wb, (45,45))
wn = pygame.transform.scale(pygame.image.load('alpha/wN.png'), (80,80))
wn_small = pygame.transform.scale(wn, (45,45))
wp = pygame.transform.scale(pygame.image.load('alpha/wP.png'), (80,80))
wp_small = pygame.transform.scale(wp, (45,45))

white_imgs = [auxilfuncs.wp, auxilfuncs.wq, auxilfuncs.wk, auxilfuncs.wn, auxilfuncs.wb, auxilfuncs.wr]
white_imgs_small = [auxilfuncs.wp_small, auxilfuncs.wq_small, auxilfuncs.wk_small, auxilfuncs.wn_small, auxilfuncs.wb_small, auxilfuncs.wr_small]

black_imgs = [auxilfuncs.bp, auxilfuncs.bq, auxilfuncs.bk, auxilfuncs.bn, auxilfuncs.bb, auxilfuncs.br]
black_imgs_small = [auxilfuncs.bp_small, auxilfuncs.bq_small, auxilfuncs.bk_small, auxilfuncs.bn_small, auxilfuncs.bb_small, auxilfuncs.br_small]

piece_list = ['pawn', 'queen', 'king', 'knight', 'bishop', 'rook']


                
#check variables


#board color

light_brown = (240,219,182)
dark_brown = (111,130,56)


#drawing the main board

def draw_board():
    for i in range(32):  #32 because we will use the background fill color for the black squares of the board
        column= i % 4
        row= i // 4
        if row % 2 == 0:
            pygame.draw.rect(screen,dark_brown,[600 - (column * 200), row* 100, 100, 100])
        else:
            pygame.draw.rect(screen,dark_brown,[700 - (column * 200), row* 100, 100, 100])

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
    
            
        
        






    #hassan I'm thinking about making a seperate texture for the board in the wooden style so this is just a placeholder
    # I've removed the discard pile tab, we dont need it. - Hassan





#gameloop

run = True

while run == True:


    timer.tick(fps)
    screen.fill(light_brown)
    draw_board()
    draw_pieces()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
   

pygame.quit()
