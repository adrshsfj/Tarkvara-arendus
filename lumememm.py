''' Paigalda arvutisse Python ja PyGame
    Tekita uus aken 300*300
    Lisa programmiaknale töönimi ja omanimi, näiteks Lumemees – Karin Eegreid
    Tee valik ning joonista samasugune objekt
    vali värvid nii, et objekt oleks nähtav
    vali suurus nii, et täidaks mõistlikkuse piires akna'''

import pygame
import sys

pygame.init()

screen = pygame.display.set_mode([300, 300])
pygame.display.set_caption("Imre Tard - Jaanus Lind")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill([0, 0, 0])
    pygame.draw.circle(screen, [255, 255, 255], [150, 75], 30, 0)
    pygame.draw.circle(screen, [255, 255, 255], [150, 140], 40, 0)
    pygame.draw.circle(screen, [255, 255, 255], [150, 225], 50, 0)
    pygame.draw.circle(screen, [0, 0, 0], [140, 70], 5, 0)
    pygame.draw.circle(screen, [0, 0, 0], [160, 70], 5, 0)
    pygame.draw.polygon(screen, [255, 0, 0], [[145,80],[150,95],[155,80], [145,80]], 0)
    pygame.display.flip()

pygame.quit()
sys.exit()

