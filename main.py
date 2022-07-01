import pygame
import math
import numpy as np

pygame.init()
pygame.display.set_caption("Trabalho OMOG")
display = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
clock = pygame.time.Clock()


color = ['red', 'orange', 'green', 'cyan', 'white', 'yellow', 'blue', 'purple', 'grey']


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


def draw_c0(coef_x, coef_y):
    for i in range(len(points)):
        x, y = points[i]
        points[i] = (x + coef_x, y + coef_y)

    print(pos_list1, points, coef_x, coef_y)


def draw_bezier(grau, pos_list):
    n = grau - 1
    for t in np.arange(0, 1, 0.01):
        z = np.zeros(2)
        for i in range(grau):
            z += np.dot((math.factorial(n) / (math.factorial(i) * math.factorial(n - i)))
                        * ((1 - t) ** (n - i)) * (t ** i), pos_list[i])
        pygame.draw.circle(display, 'red', z.astype(int), 3)



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


def draw_bspline(grau, pos_list):
    z = np.zeros(2)

    n = grau + len(pos_list) + 1
    factor = 1 / n

    inicio = 0
    balance = factor * (grau + 2)

    for i in range(grau, len(pos_list)):
        for t in np.arange(inicio, balance, 0.01):
            z = deBoor(i, t, knots, pos_list, grau)
            pygame.draw.circle(display, color[i], z, 3)

        if i == len(pos_list) - 2:
            inicio = factor * (len(pos_list) - 1)
            balance = factor * (len(pos_list) + grau + 1)
        else:
            inicio = balance
            balance += factor

'''

Bezier

'''

pos_list1 = []  # Bezier

'''

B-spline 

'''

points = []
degree = 4
knots = [] # will be generated later when we get the control points


flag = True
run = True

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if len(pos_list1) < 6:
                pos_list1.append(event.pos)
            else:
                points.append(event.pos)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                print(pos_list1, points)
                points.clear()
                pos_list1.clear()
                flag = True
            if event.key == pygame.K_b:
                if len(pos_list1) == 6 and len(points) == 9:
                    if flag:
                        x1, y1 = pos_list1[-1]
                        x2, y2 = points[0]
                        coef_x, coef_y = (x1 - x2), (y1 - y2)

                        print(pos_list1, points, coef_x, coef_y)

                        draw_c0(coef_x, coef_y)
                        flag = False

    display.fill(0)
    for x, y in pos_list1:
        pygame.draw.circle(display, 'pink', (x, y), 8)

    for x, y in points:
        pygame.draw.circle(display, 'pink', (x, y), 8)

    # for i in range(len(pos_list1) - 1):
    #     if len(pos_list1) >= 2:
    #         pygame.draw.line(display, "green",
    #                          start_pos=pos_list1[i], end_pos=pos_list1[i + 1])

    # for i in range(len(pos_list2) - 1):
    #     if len(pos_list2) >= 2:
    #         pygame.draw.line(display, "green",
    #                          start_pos=pos_list2[i], end_pos=pos_list2[i + 1])

    if len(pos_list1) == 6:
        draw_bezier(len(pos_list1), pos_list1)

    if len(points) == 9:
        knots = generate_knots_with_rep(degree, len(points))
        draw_bspline(degree, points)

    pygame.display.update()

    clock.tick(30)

pygame.quit()
exit()
