import pygame

class Piece ():

    def __init__(self, img ,x, y):
        self.x = x
        self.y = y
        self.img = img
        self.clicked = False
        self.origin = (self.x, self.y)

    def draw (self, screen):
        screen.blip(self.img, (self.x, self.y))

    def move (x, y):
        self.x = x
        self.y = y

    def capture (self, opp_x, opp_y):
        self.x = opp_x
        self.y = opp_y

class Pawn (Piece):

    def __init__(self, img, x, y):
        super().__init__(self, img, x, y)
    
    
        

class Board ():

    def __init__(self):
        self.screen = self.make_screen ()
        self.board = self.make_board ()

    def make_screen (self):
        pygame.init()
        logo = pygame.image.load("logo.png")
        pygame.display.set_icon(logo)
        pygame.display.set_caption("chess game")
        return pygame.display.set_mode((512, 512))

    def make_board (self):
        
        temp = []
        for i in range (0, 512, 64):
            for j in range (0, 512, 64):
                temp.append(pygame.Rect(i, j, 64, 64))
        self.squares = temp

    def draw_board (self):

        white = (255, 255, 255)
        black = (0, 50, 20)

        count = 0
        color = None 
        self.make_board()

        for square in self.squares:
            color = white if color == black else black   
            if count % 8 == 0:
                color = white if color == black else black   
            pygame.draw.rect(self.screen, color, square)
            count += 1

    def load_board_white (self):
        wp = pygame.image.load('resources/white_pawn.png')

        wr = pygame.image.load('resources/white_rook.png')
        wh = pygame.image.load('resources/white_horse.png')
        wb = pygame.image.load('resources/white_bishop.png')

        wq = pygame.image.load('resources/white_queen.png')
        wk = pygame.image.load('resources/white_king.png')

        white_map = []

        for i in range (0, 512, 64):
            white_map.append((wp,(384,i)))

        # draw rooks
        white_map.append((wr, (448, 0)))
        white_map.append((wr, (448, 448)))

        # draw horses
        white_map.append((wh, (448,64)))
        white_map.append((wh, (448,384)))

        # draw bishops 
        white_map.append((wb, (448, 128)))
        white_map.append((wb, (448, 320)))

        # draw queen and king
        white_map.append((wk, (448, 192)))
        white_map.append((wq, (448, 256)))
        
        return white_map

    def load_board_black (self):
        self.draw_board()
        black_map = []

        bp = pygame.image.load('resources/black_pawn.png')

        br = pygame.image.load('resources/black_rook.png')
        bh = pygame.image.load('resources/black_horse.png')
        bb = pygame.image.load('resources/black_bishop.png')

        bq = pygame.image.load('resources/black_queen.png')
        bk = pygame.image.load('resources/black_king.png')

        # draw pawns
        for i in range (0, 512, 64):
            black_map.append((bp, (64, i)))
        
        # draw rooks
        black_map.append((br, (0,0)))
        black_map.append((br, (0,448)))

        # draw horses
        black_map.append((bh, (0, 64)))
        black_map.append((bh, (0, 384)))

        # draw bishops
        black_map.append((bb, (0, 128)))
        black_map.append((bb, (0, 320)))

        # draw king & queen
        black_map.append((bk, (0, 192)))
        black_map.append((bq, (0, 256)))

        return black_map

def draw (team, screen):
    for piece in team:
        screen.blit(piece[0], piece[1])

def main ():

    board = Board ()
    running = True


    while running:
        for event in pygame.event.get():

            black = board.load_board_black()
            white = board.load_board_white()

            if event.type == pygame.QUIT:
                running = False
            if  pygame.MOUSEBUTTONDOWN:
                locate = pygame.mouse.get_pos()
                for square in board.squares:
                    if square.collidepoint(locate):
                        pygame.draw.rect(board.screen, (255,50,0), square)
                    # if user clicks mouse
                    # change the color of square to blue

                draw (black, board.screen)
                draw (white, board.screen)
                #record open spots

            pygame.display.flip()
    

if __name__ == '__main__':
    main ()
