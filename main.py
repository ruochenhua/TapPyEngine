	
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys, pygame
pygame.init()

from MeshCreator import MeshCreator

size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

mesh_creator = MeshCreator()
all_sprites = mesh_creator.CreateRectMesh((15, 30), (1, 2))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    screen.fill(black)
    all_sprites.draw(screen)
    pygame.display.flip()


pygame.quit()