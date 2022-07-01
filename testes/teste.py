import pygame
import math
import numpy as np

pygame.init()
pygame.display.set_caption("Trabalho OMOG")
display = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
clock = pygame.time.Clock()

'''

B-spline 

'''


def generate_knots_without_rep(degree, tam_list):
    n = tam_list + degree + 1
    factor = 1 / (n - 1)
    list = []
    for i in np.arange(0.0, 1.0 + factor, factor):
        list.append(i)

    return list


def generate_knots_with_rep(degree, tam_list):
    n = tam_list + degree + 1
    factor = 1 / (n-1)
    list = [0.0 for i in range(degree + 1)]
    aux_count = []
    for i in np.arange(0.0, 1.0 + factor, factor):
        aux_count.append(round(i, 3))

    for i in range(degree+1, n -degree -1):
        list.append(aux_count[i])

    list_aux_one = [1.0 for i in range(degree + 1)]

    list = list + list_aux_one

    return list


# points = [(232, 256), (285, 148), (357, 258), (472, 156), (523, 248), (658, 143)]
points = [(232, 256), (285, 148), (357, 258), (472, 156), (523, 248), (658, 143),
          (775.5469110953279, 318.59430491341345), (486.3735930418964, 484), (315, 364)]
degree = 4
# knots = [0.0, 0.0, 0.0, 0.0, 0.0, 0.385, 0.462, 0.538, 0.615, 1, 1, 1, 1, 1]  # 6 + 2 +1
knots = generate_knots_with_rep(degree, len(points))
#knots = generate_knots_without_rep(degree, len(points))
print(f'knots = {knots}')

# Calcular a proporcao dos knots usando 1/(len(points) + degree)

color = ['red', 'orange', 'green', 'cyan', 'white', 'yellow', 'blue', 'purple', 'grey']

flag = True
run = True


def draw_bspline(grau, pos_list):
    z = np.zeros(2)

    n = degree + len(points) + 1
    factor = 1 / n

    inicio = 0
    balance = factor * (degree + 2)

    for i in range(degree, len(points)):
        for t in np.arange(inicio, balance, 0.01):
            z = deBoor(i, t, knots, points, degree)
            pygame.draw.circle(display, color[i], z, 3)

        if i == len(points) - 2:
            inicio = factor * (len(points) - 1)
            balance = factor * (len(points) + degree + 1)
        else:
            inicio = balance
            balance += factor


def deBoor(k: int, x: int, t, c, p: int):
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


while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if len(points) < 6:
                points.append(event.pos)

    display.fill(0)

    for x, y in points:
        pygame.draw.circle(display, 'pink', (x, y), 8)

    for i in range(len(points) - 1):
        if len(points) >= 2:
            pygame.draw.line(display, "green", start_pos=points[i], end_pos=points[i + 1])

    if len(points) > 4:
        draw_bspline(degree, pos_list=points)

    pygame.display.update()
    clock.tick(30)

pygame.quit()
exit()
