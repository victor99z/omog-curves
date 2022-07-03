import numpy as np
import pygame


class Bspline:
    def __init__(self, control_points, degree=4):
        self.knots = None
        self.degree = degree
        self.control_points = control_points

    def cox_de_boor(self, k: int, x: int, t, c, p: int):
        """Evaluates S(x).

        Arguments
        ---------
        k: Index of knot interval that contains x.
        x: Position.
        t: Array of knot positions, needs to be padded as described above.
        c: Array of control points.
        p: Degree of B-spline.
        """
        d = [c[j + k - p] for j in range(0, p + 1)]

        for r in range(1, p + 1):
            for j in range(p, r - 1, -1):
                alpha = (x - t[j + k - p]) / (t[j + 1 + k - r] - t[j + k - p])
                d[j] = np.dot((1.0 - alpha), d[j - 1]) + np.dot(alpha, d[j])

        return d[p]

    def generate_knots_with_rep(self):
        tam_list = len(self.control_points)
        n = tam_list + self.degree + 1
        factor = 1 / (n - 1)
        aux_count = []

        list = [0.0 for i in range(self.degree + 1)]

        for i in np.arange(0.0, 1.0 + factor, factor):
            aux_count.append(round(i, 3))

        for i in range(self.degree + 1, n - self.degree - 1):
            list.append(aux_count[i])

        list_aux_one = [1.0 for i in range(self.degree + 1)]

        return list + list_aux_one

    def draw_bspline(self, display):

        self.knots = self.generate_knots_with_rep()

        n = self.degree + len(self.control_points) + 1
        factor = 1 / n

        init = 0
        balance = factor * (self.degree + 2)

        for i in range(self.degree, len(self.control_points)):
            for t in np.arange(init, balance, 0.01):
                z = self.cox_de_boor(i, t, self.knots, self.control_points, self.degree)
                pygame.draw.circle(display, 'cyan', z, 2)

            if i == len(self.control_points) - 2:
                init = factor * (len(self.control_points) - 1)
                balance = factor * (len(self.control_points) + self.degree + 1)
            else:
                init = balance
                balance += factor
