import pygame

def main ():
    pygame.init()
    logo = pygame.image.load("logo.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("chess game")
    screen = pygame.display.set_mode((512, 512))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    


if __name__ == '__main__':
    main ()
