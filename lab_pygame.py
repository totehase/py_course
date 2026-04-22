import pygame


run = True
w = 400
h = 100
pygame.init()
sc = pygame.display.set_mode((w, h))
f = pygame.font.SysFont(None, 48)
t = f.render("Я Лиза:)", True, (255, 255, 255))
sc.blit(t, ((w - t.get_width()) // 2, (h - t.get_height())))
pygame.display.flip()

while run:
    for e in pygame.event.get():
        if (e.type == pygame.QUIT
            or e.type == pygame.MOUSEBUTTONUP
            or e.type == pygame.KEYUP):
            run = False