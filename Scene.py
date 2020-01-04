#!/usr/bin/python
# -*- coding: UTF-8 -*-

from SimObject import Object
import PhysicsIntergration

class Scene():
    _scene_name = ""
    _scene_objects = []

    def __init__(self, scene_name):
        self._scene_name = scene_name

    def append_object(self, obj):
        self._scene_objects.append(obj)

    def get_objects(self):
        return self._scene_objects

class Scene1(Scene):
    
    def __init__(self):
        super().__init__("scene 1")

        # init scene
        obj1 = Object()
        obj1.init_mesh([(17, 49), (48, 58), (70, 35),
         (59, 7), (29, 2), (10, 25)])
        
        self.append_object(obj1)


        obj2 = Object()
        obj2.init_mesh([(10, 10), (100, 10), (100, 30),
         (10, 30)])        
        self.append_object(obj2)

        obj2.set_center((0, 100))
        obj2.set_static(True)


