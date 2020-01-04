#!/usr/bin/python
# -*- coding: UTF-8 -*-

sprite_size = 10
sprite_color = (0, 255, 255)

class Mesh():
    _points = []

    def __init__(self, points):
        self._points = points


class Transform():
    def __init__(self):
        self._center = 0, 0
        self._rotation = 0

class PhysicsProperty():
    def __init__(self):
        self._linear_velocity = 0, 0
        self._angular_velocity = 0
        self._mass = 1
        self._force = 0, 0
        self._torque = 0
        self._is_static = False

class Object():
    _mesh = None
    _trans = None
    _phy_prop = None

    _color = sprite_color

    def __init__(self):
        self._trans = Transform()
        self._phy_prop = PhysicsProperty()

    def init_mesh(self, points):
        self._mesh = Mesh(points)

    def set_center(self, center):
        self._trans._center = center

    def get_center(self):
        return self._trans._center

    def get_render_points(self):
        points = []
        
        for p in self._mesh._points:
            p_t = ((p[0] + self._trans._center[0]), 
            p[1] + self._trans._center[1])
            points.append(p_t)

        return points

    def set_static(self, is_static):
        self._phy_prop._is_static = is_static
