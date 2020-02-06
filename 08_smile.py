# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd
import datetime
import math
import os
import tempfile
import time
from random import choice, randint
import random
import pygame
from pygame import locals as pgl

sd.resolution = (1200, 600)
# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана

# point = sd.get_point(600, -20)
# radius = 600
# colors = [sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN, sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE,]
# for i in colors:
#    radius -= 30
#    sd.circle(center_position = point, radius = radius, color=i, width=30)
#sd.pause()


sd.resolution = (1200, 600)
def bubble(point, step):
    radius = 50
    for _ in range(3):
        radius += 0
        sd.circle(center_position=point, radius=radius)
for _ in range(10):
    point = sd.random_point()
    step = random.randint(2, 16)
    bubble(point=point, step=step)
