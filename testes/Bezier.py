import math
import numpy as np
import pygame


class Bezier:

    points = []
    degree = len(points)

    def draw_bezier(self, display):
        n = self.degree - 1
        for t in np.arange(0, 1, 0.01):
            z = np.zeros(2)
            for i in range(self.degree):
                z += np.dot((math.factorial(n) / (math.factorial(i) * math.factorial(n - i)))
                            * ((1 - t) ** (n - i)) * (t ** i), self.points[i])

            pygame.draw.circle(display, 'red', z.astype(int), 3)
