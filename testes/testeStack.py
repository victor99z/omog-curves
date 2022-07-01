import numpy as np
import pygame
import math as m

points = np.array([[i, m.sin(i / 3.0), m.cos(i / 2)] for i in range(0, 11)])
knots = np.array([0, 0, 0, 0, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 1.0, 1.0, 1.0, 1.0])


pygame.init()
pygame.display.set_caption("Trabalho OMOG")
display = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
clock = pygame.time.Clock()


def deBoorDerivative(k, x, t, c, p):
    """
    Evaluates S(x).

    Args
    ----
    k: index of knot interval that contains x
    x: position
    t: array of knot positions, needs to be padded as described above
    c: array of control points
    p: degree of B-spline
    """
    q = [p * (c[j + k - p + 1] - c[j + k - p]) / (t[j + k + 1] - t[j + k - p + 1]) for j in range(0, p)]

    for r in range(1, p):
        for j in range(p - 1, r - 1, -1):
            right = j + 1 + k - r
            left = j + k - (p - 1)
            alpha = (x - t[left]) / (t[right] - t[left])
            q[j] = (1.0 - alpha) * q[j - 1] + alpha * q[j]

    print(q[p-1])
    # pygame.draw.circle(display, 'red', q[p-1], 3)
    return q[p - 1]


def finiteDifferenceDerivative(k, x, t, c, p):
    """ Third order finite difference derivative """

    f = lambda xx: deBoorDerivative(k, xx, t, c, p)

    dx = 1e-7

    return (- f(x + 2 * dx)
            + 8 * f(x + dx)
            - 8 * f(x - dx)
            + f(x - 2 * dx)) / (12 * dx)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass

    display.fill(0)

    deBoorDerivative(7, 0.44, knots, points, 3)

    pygame.display.update()
    clock.tick(30)

pygame.quit()
exit()

print("Derivatives: ")
print("De Boor:\t", deBoorDerivative(7, 0.44, knots, points, 3))
print("Finite Difference:\t", finiteDifferenceDerivative(7, 0.44, knots, points, 3))

