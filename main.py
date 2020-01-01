	
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys, pygame
pygame.init()

from MeshCreator import Mesh

from Scene import Scene1

size = width, height = 720, 480
speed = [2, 2]
black = 0, 0, 0
screen = pygame.display.set_mode(size)


scene_1 = Scene1()
# scene_1.init_scene()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # all_sprites.update()

    screen.fill(black)

    meshes = scene_1.get_meshes()

    for mesh in meshes:
        pygame.draw.polygon(screen, mesh._color, mesh._points)

    pygame.display.flip()



pygame.quit()