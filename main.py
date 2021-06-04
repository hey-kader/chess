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

    def move (x, y)
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
        return temp

    def draw_board (self):

        white = (255, 255, 255)
        black = (0, 50, 20)

        count = 0
        color = None 
        self.squares = self.make_board()

        for square in squares:
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

        for i in range (0, 512, 64):
            self.screen.blit(wp,(384,i))

        # draw rooks
        self.screen.blit(wr, (448, 0))
        self.screen.blit(wr, (448, 448))

        # draw horses
        self.screen.blit(wh, (448,64))
        self.screen.blit(wh, (448,384))

        # draw bishops 
        self.screen.blit (wb, (448, 128))
        self.screen.blit (wb, (448, 320))

        # draw queen and king
        self.screen.blit (wk, (448, 192))
        self.screen.blit (wq, (448, 256))

    def load_board_black (self):
        self.draw_board()

        bp = pygame.image.load('resources/black_pawn.png')

        br = pygame.image.load('resources/black_rook.png')
        bh = pygame.image.load('resources/black_horse.png')
        bb = pygame.image.load('resources/black_bishop.png')

        bq = pygame.image.load('resources/black_queen.png')
        bk = pygame.image.load('resources/black_king.png')

        # draw pawns
        for i in range (0, 512, 64):
            self.screen.blit(bp, (64,i))
        
        # draw rooks
        self.screen.blit(br, (0,0))
        self.screen.blit(br, (0,448))

        # draw horses
        self.screen.blit(bh, (0,64))
        self.screen.blit(bh, (0,384))

        # draw bishops
        self.screen.blit(bb, (0, 128))
        self.screen.blit(bb, (0, 320))

        # draw king & queen
        self.screen.blit(bk, (0, 192))
        self.screen.blit(bq, (0, 256))



def main ():

    board = Board ()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        board.load_board_black()
        board.load_board_white()
        pygame.display.flip()
    

if __name__ == '__main__':
    main ()
