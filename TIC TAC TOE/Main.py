import pygame, sys
from button import Button
import numpy as np
from playsound import playsound

pygame.init()

SCREEN = pygame.display.set_mode((1050,700))
pygame.display.set_caption("Home")

BG = pygame.image.load("tt10.jpeg")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def play():
    WIDTH = 600
    HEIGHT = 700
    LINE_WIDTH = 15
    WIN_LINE_WIDTH = 15
    SQUARE_SIZE = 200
    LINE_COLOR = (0,0,0)
    BACKGROUND_COLOR = (255,255,255)
    BOARD_ROWS=3
    BOARD_COLS=3
    CIRCLE_COLOR = (119,136,153)
    CROSS_COLOR = 	(233,150,122)
    CIRCLE_RADIUS = 60
    CIRCLE_WIDTH = 15
    CROSS_WIDTH = 25
    SPACE = 55

    screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
    screen.fill(BACKGROUND_COLOR)
    pygame.display.set_caption("TIC TAC TOE")

    font = pygame.font.SysFont(None,30)
    img = font.render('1st player is O',True,CIRCLE_COLOR)
    screen.blit(img,(40,600))

    font = pygame.font.SysFont(None,30)
    img = font.render('2nd player is X',True,CROSS_COLOR)
    screen.blit(img,(40,625))

    board=np.zeros((BOARD_ROWS,BOARD_COLS))

    def draw_lines():
        pygame.draw.line(screen, LINE_COLOR, (20,SQUARE_SIZE), (580,SQUARE_SIZE), 10 )
        pygame.draw.line(screen, LINE_COLOR, (200,20), (200,580), 10 )
        pygame.draw.line(screen, LINE_COLOR, (20,400), (580,400), 10 )
        pygame.draw.line(screen, LINE_COLOR, (400,20), (400,580), 10 )

    draw_lines()

    def draw_figures():
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if board[row][col] == 1:
                    pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * 200 + 100), int(row * 200 + 100)), CIRCLE_RADIUS,
                                       CIRCLE_WIDTH)
                elif board[row][col] == 2:
                    pygame.draw.line(screen,CROSS_COLOR,(col * 200 + SPACE ,row * 200 + 200 - SPACE),(col * 200 + 200 - SPACE,row * 200 + SPACE),CROSS_WIDTH)
                    pygame.draw.line(screen,CROSS_COLOR,(col * 200 + SPACE ,row * 200 +  SPACE),(col * 200 + 200 - SPACE,row * 200 + 200 - SPACE),CROSS_WIDTH)

    def mark_square(row, col,player):
        board[row][col]=player

    def available_square(row,col):
        return board[row][col]==0

    def is_board_full(row,col):
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if board[row][col]==0:
                    return False
        return True

    def draw_vertical_winning_line(col,player):
        posX = col * 200 + 100
        if player==1:
            color = CIRCLE_COLOR
       
            font = pygame.font.SysFont(None,30)
            img = font.render('Player 1 wins...!!',True, (128,0,0))
            screen.blit(img,(250,650))

        else:
            color = CROSS_COLOR
        
            font = pygame.font.SysFont(None,30)
            img = font.render('Player 2 wins...!!',True,(75,0,130))
            screen.blit(img,(250,650))
        pygame.draw.line(screen,color,(posX,15),(posX,575),15)

    def draw_horizontal_winning_line(row,player):
        posY = row * 200 + 100
        if player==1:
            color = CIRCLE_COLOR
            font = pygame.font.SysFont(None,30)
            img = font.render('Player 1 wins...!!',True, (128,0,0))
            screen.blit(img,(250,650))
        else:
            color = CROSS_COLOR
       
            font = pygame.font.SysFont(None,30)
            img = font.render('Player 2 wins...!!',True,(75,0,130))
            screen.blit(img,(250,650))

        pygame.draw.line(screen,color,(15,posY),(575,posY),15)

    def draw_asc_diagonal(player):
        if player==1:
            color = CIRCLE_COLOR
        
            font = pygame.font.SysFont(None,30)
            img = font.render('Player 1 wins...!!',True, (128,0,0))
            screen.blit(img,(250,650))
        else:
            color = CROSS_COLOR
        
            font = pygame.font.SysFont(None,30)
            img = font.render('Player 2 wins...!!',True, (75,0,130))
            screen.blit(img,(250,650))
        pygame.draw.line(screen,color,(15,575),(575,15),15)

    def draw_desc_diagonal(player):
        if player==1:
            color = CIRCLE_COLOR
        
            font = pygame.font.SysFont(None,30)
            img = font.render('Player 1 wins...!!',True, (128,0,0))
            screen.blit(img,(250,650))
        else:
            color = CROSS_COLOR
        
            font = pygame.font.SysFont(None,30)
            img = font.render('Player 2 wins...!!',True,((75,0,130)))
            screen.blit(img,(250,650))
        pygame.draw.line(screen,color,(15,15),(575,575),15)

    def restart():
        screen.fill(BACKGROUND_COLOR)
        draw_lines()
        player = 1
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                board[row][col] = 0
    

    def check_win(player):
        #vertical line win check
        for col in range(BOARD_COLS):
            if board[0][col]==player and board[1][col]==player and board[2][col]==player:
                draw_vertical_winning_line(col,player)
                return True

    #horizontal line win check
        for row in range(BOARD_ROWS):
            if board[row][0]==player and board[row][1]==player and board[row][2]==player:
                draw_horizontal_winning_line(row,player)
                return True
    
    #Asc diagonal win check
        if board[2][0]==player and board[1][1]==player and board[0][2]==player:
            draw_asc_diagonal(player)
            return True

    #Desc diagonal win check
        if board[0][0]==player and board[1][1]==player and board[2][2]==player:
            draw_desc_diagonal(player)
            return True
        return False
   
    player = 1
    game_over = False
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        OPTIONS_BACK = Button(image=None, pos=(530,650), 
                            text_input="QUIT", font=get_font(20), base_color="black", hovering_color="blue")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                MouseX = event.pos[0]
                MouseY = event.pos[1]

                clicked_row=int(MouseY // 200)
                clicked_col=int(MouseX // 200)

                if available_square(clicked_row,clicked_col):
                    if player == 1:
                        mark_square(clicked_row,clicked_col,1)
                        if check_win(player):
                            game_over = True
                        player=2
                                              
                    else:
                        mark_square(clicked_row,clicked_col,2)
                        if check_win(player):
                            game_over = True
                        player=1
                    
                    draw_figures()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    restart()
        
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()



        pygame.display.update()

    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("silver")
        text = "Tic tac toe"
        text2 = "->It's a game played between 2 persons where each "
        text3 = "one selects their respective symbols and makes moves"
        text4 = "across the board of 9 partitions by selecting"
        text5 = "and dumping their symbol into the respective box."
        text6 = "->If their symbol is present in one full row or column"
        text7 = "or diagonal then they are declared as the winners"
        text8 = "Go ahead Play the game....!!"
        text9 = "(Press BACK to reach the menu)"


        OPTIONS_TEXT = get_font(25).render(text, True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(525,50))
        OPTIONS_TEXT_1 = get_font(16).render(text2, True, "Black")
        OPTIONS_RECT_1 = OPTIONS_TEXT.get_rect(center=(150,100))
        OPTIONS_TEXT_3 = get_font(16).render(text3, True, "Black")
        OPTIONS_RECT_3 = OPTIONS_TEXT.get_rect(center=(150,150))
        OPTIONS_TEXT_4 = get_font(16).render(text4, True, "Black")
        OPTIONS_RECT_4 = OPTIONS_TEXT.get_rect(center=(150,200))
        OPTIONS_TEXT_5 = get_font(16).render(text5, True, "Black")
        OPTIONS_RECT_5 = OPTIONS_TEXT.get_rect(center=(150,250))
        OPTIONS_TEXT_6 = get_font(16).render(text6, True, "Black")
        OPTIONS_RECT_6 = OPTIONS_TEXT.get_rect(center=(150,300))
        OPTIONS_TEXT_7 = get_font(16).render(text7, True, "Black")
        OPTIONS_RECT_7 = OPTIONS_TEXT.get_rect(center=(150,350))
        OPTIONS_TEXT_8 = get_font(20).render(text8, True, "Black")
        OPTIONS_RECT_8 = OPTIONS_TEXT.get_rect(center=(450,400))
        OPTIONS_TEXT_9 = get_font(10).render(text9, True, "Black")
        OPTIONS_RECT_9 = OPTIONS_TEXT.get_rect(center=(520,540))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)
        SCREEN.blit(OPTIONS_TEXT_1, OPTIONS_RECT_1)
        SCREEN.blit(OPTIONS_TEXT_3, OPTIONS_RECT_3)
        SCREEN.blit(OPTIONS_TEXT_4,OPTIONS_RECT_4)
        SCREEN.blit(OPTIONS_TEXT_5,OPTIONS_RECT_5)
        SCREEN.blit(OPTIONS_TEXT_6,OPTIONS_RECT_6)
        SCREEN.blit(OPTIONS_TEXT_7,OPTIONS_RECT_7)
        SCREEN.blit(OPTIONS_TEXT_8,OPTIONS_RECT_8)
        SCREEN.blit(OPTIONS_TEXT_9,OPTIONS_RECT_9)

        OPTIONS_BACK = Button(image=None, pos=(520, 500), 
                            text_input="BACK", font=get_font(20), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(30).render("", True, "#FFFFFF")
        MENU_RECT = MENU_TEXT.get_rect(center=(400,50))

        PLAY_BUTTON = Button(image=pygame.image.load("Options Rect1.png"), pos=(750,190), 
                            text_input="PLAY GAME", font=get_font(20), base_color="#000000", hovering_color="blue")
        OPTIONS_BUTTON = Button(image=pygame.image.load("Options Rect1.png"), pos=(750, 320), 
                            text_input="DESCRIPTION", font=get_font(20), base_color="#000000", hovering_color="blue")
        QUIT_BUTTON = Button(image=pygame.image.load("Options Rect1.png"), pos=(750, 450), 
                            text_input="QUIT", font=get_font(20), base_color="#000000", hovering_color="blue")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()
playsound('start.wav')
main_menu()