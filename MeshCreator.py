#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pygame

sprite_size = 10
sprite_color = (0, 255, 255)

class MeshDot(pygame.sprite.Sprite):
    def __init__(self, dot_center):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((sprite_size, sprite_size))
        self.image.fill(sprite_color)

        self.rect = self.image.get_rect()
        self.rect.center = (dot_center[0]*sprite_size, dot_center[1]*sprite_size)


class MeshCreator():
    def __init__(self):
        pass

    def CreateRectMesh(self, max_dot, min_dot):
        mesh_dot = pygame.sprite.Group()
        for i in range(min_dot[0], max_dot[0]):
            for j in range(min_dot[1], max_dot[1]):
                mesh_dot.add(MeshDot((i, j)))

        return mesh_dot



