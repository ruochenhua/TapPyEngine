#!/usr/bin/python
# -*- coding: UTF-8 -*-

from MeshCreator import Mesh

class Scene():
    _scene_name = ""
    _scene_meshes = []

    def __init__(self, scene_name):
        self._scene_name = scene_name

    def append_mesh(self, mesh):
        self._scene_meshes.append(mesh)

    def get_meshes(self):
        return self._scene_meshes

class Scene1(Scene):
    
    def __init__(self):
        super().__init__("scene 1")

        # init scene
        mesh = Mesh([(152, 190), (152, 230), (158, 230)])
        super().append_mesh(mesh)
        

