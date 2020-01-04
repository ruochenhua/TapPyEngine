	
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys, pygame
pygame.init()

import time
current_milli_time = lambda: float(round(time.time()*1000000))


from PhysicsIntergration import PhysicsIntergration
from SimObject import Object

from Scene import Scene1

size = width, height = 720, 480
speed = [2, 2]
black = 0, 0, 0
screen = pygame.display.set_mode(size)


scene_1 = Scene1()
# scene_1.init_scene()
physics_int = PhysicsIntergration()

running = True
time_stamp = current_milli_time()

while running:
    cur_time = current_milli_time()
    delta_time = cur_time - time_stamp
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # all_sprites.update()
    delta_time = (float(delta_time)/1000000.0)

    screen.fill(black)

    objects = scene_1.get_objects()

    for obj in objects:
        physics_int.step_time(delta_time, obj)
        pygame.draw.polygon(screen, obj._color, obj.get_render_points())

    pygame.display.flip()

    time_stamp = cur_time



pygame.quit()