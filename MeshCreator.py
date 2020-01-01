#!/usr/bin/python
# -*- coding: UTF-8 -*-

sprite_size = 10
sprite_color = (0, 255, 255)

class Mesh():
    _points = []
    _color = sprite_color

    def __init__(self, points):
        self._points = points


