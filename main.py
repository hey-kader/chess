import pygame

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
        black = (0, 0, 0)

        count = 0
        color = None 
        for square in self.make_board():
            color = white if color == black else black   
            if count % 8 == 0:
                color = white if color == black else black   
            pygame.draw.rect(self.screen, color, square)
            count += 1


def main ():

    board = Board ()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        board.draw_board()
        pygame.display.flip()
    

if __name__ == '__main__':
    main ()
