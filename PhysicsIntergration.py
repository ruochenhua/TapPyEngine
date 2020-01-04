#!/usr/bin/python
# -*- coding: UTF-8 -*-

from SimObject import *

gravity = (0, 30)

class PhysicsIntergration():
    _env = ""

    def __init__(self):
        self._env = "Physics Intergration"

    def step_time(self, delta_time, obj):
        self.intergate(delta_time, obj)

    def intergate(self, delta_time, obj):
        if(obj._phy_prop._is_static):
            return

        total_force = (obj._phy_prop._force[0] + gravity[0],
        obj._phy_prop._force[1] + gravity[1])

        obj._phy_prop._force = 0, 0
        obj._phy_prop._torque = 0

        mass = obj._phy_prop._mass
        acc = (total_force[0] / mass, total_force[1])

        obj_vel = obj._phy_prop._linear_velocity

        vel = (obj_vel[0] + delta_time*acc[0], obj_vel[1] + delta_time*acc[1])

        obj._phy_prop._linear_velocity = vel
        
        obj_center = obj._trans._center
        center = (obj_center[0] + vel[0]*delta_time, 
        obj_center[1] + vel[1]*delta_time)
        obj._trans._center = center

