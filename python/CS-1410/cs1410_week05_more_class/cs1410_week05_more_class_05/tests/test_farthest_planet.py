# # python -m unittest discover -vbs tests

import unittest

from farthest_planet import *

import random, math

def random_planet():
    scale = 100.
    planet = { 'x': random.random() * scale,
               'y': random.random() * scale,
               'z': random.random() * scale }
    return planet

def d(p):
    dist  = p['x']*p['x']
    dist += p['y']*p['y']
    dist += p['z']*p['z']
    return math.sqrt(dist)

def random_solar_system(number_of_planets):
    solar_system = []
    pluto = None
    for i in range(number_of_planets):
        p = random_planet()
        if pluto is None or d(p) > d(pluto):
            pluto = p
        solar_system.append(p)

    return solar_system, pluto


class Test_FarthestPlanet(unittest.TestCase):

    def test_01(self):
        for i in range(10):
            solar_system, correct_answer = random_solar_system(random.randrange(1, 100))
            your_answer = farthest_planet(solar_system)
            self.assertEqual(correct_answer, your_answer)

        return
