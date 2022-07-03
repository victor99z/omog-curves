# Fixed degree of 5 (6 control points)
import numpy as np
import math
import pygame


class Bezier:
    def __init__(self, control_points, degree=6):
        self.degree = degree
        self.control_points = control_points

    def draw_bezier(self, display):
        n = self.degree - 1
        for t in np.arange(0, 1, 0.01):
            z = np.zeros(2)
            for i in range(self.degree):
                z += np.dot((math.factorial(n) / (math.factorial(i) * math.factorial(n - i)))
                            * ((1 - t) ** (n - i)) * (t ** i), self.control_points[i])
            pygame.draw.circle(display, 'red', z.astype(int), 2)


