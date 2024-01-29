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
pygame.display.set_caption("Asd - Jaanus Lind")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill([0, 0, 0])
    pygame.draw.circle(screen, [255, 0, 0], [150, 65], 40, 0)
    pygame.draw.circle(screen, [255, 255, 0], [150, 150], 40, 0)
    pygame.draw.circle(screen, [0, 255, 0], [150, 235], 40, 0)
    pygame.draw.rect(screen, [128, 128, 128], [100, 15, 100, 270], 2)
    pygame.display.flip()

pygame.quit()
sys.exit()

