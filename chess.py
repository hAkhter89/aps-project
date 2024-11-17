import pygame

pygame.init()

screen_width=900
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
white_coords = [(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),
                (0,1),(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1)]

black_coords = [(0,7),(1,7),(2,7),(3,7),(4,7),(5,7),(6,7),(7,7),
                (0,6),(1,6),(2,6),(3,6),(4,6),(5,6),(6,6),(7,6)]


capture_white = []
capture_black = []

#turns


turn_step = 0
selected = 100

legal_moves = []

#textures and assets



                
#check variables


#board color

light_brown = (240,219,182)
dark_brown = (55,26,8)


#drawing the main board

def draw_board():
    for i in range(32):  #32 because we will use the background fill color for the black squares of the board
        column= i % 4
        row= i // 4
        if row % 2 == 0:
            pygame.draw.rect(screen,light_brown,[600 - (column * 200), row* 100, 100, 100])
        else:
            pygame.draw.rect(screen,light_brown,[700 - (column * 200), row* 100, 100, 100])






    #hassan I'm thinking about making a seperate texture for the board in the wooden style so this is just a placeholder






#gameloop

run = True

while run == True:


    timer.tick(fps)
    screen.fill(dark_brown)
    draw_board()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
   

pygame.quit()
