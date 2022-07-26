import pygame
from Bspline import Bspline
from Bezier import Bezier
import math

pygame.init()
pygame.display.set_caption("Trabalho OMOG")
display = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
clock = pygame.time.Clock()

color = ['red', 'orange', 'green', 'cyan', 'white', 'yellow', 'blue', 'purple', 'grey']


def draw_c0():
    x1, y1 = bezier.control_points[-1]
    x2, y2 = bspline.control_points[0]
    coef_x, coef_y = (x1 - x2), (y1 - y2)

    print(f' {bezier.control_points} {bspline.control_points} {coef_x, coef_y}')

    for i in range(len(bspline.control_points)):
        x, y = bspline.control_points[i]
        bspline.control_points[i] = (x + coef_x, y + coef_y)

    print(f'c1: \n {bezier.control_points} {bspline.control_points} {coef_x, coef_y}')


def draw_c1():
    draw_c0()
    v1, v2 = bezier.control_points[-1], bezier.control_points[-2]  # (x,y), (x,y)
    j1, j2 = bspline.control_points[0], bspline.control_points[1]  # (x,y), (x,y)

    # v1 = B | v2 = A
    # j1 ~ B | j2 = P2
    vetor_bezier_normalizado = (v1[0] - v2[0]), (v1[1] - v2[1])  # AB
    raiz = math.sqrt(
        math.pow(vetor_bezier_normalizado[0], 2) + math.pow(vetor_bezier_normalizado[1], 2))  # magnitude do AB
    vetor_bezier_normalizado = vetor_bezier_normalizado[0] / raiz, vetor_bezier_normalizado[
        1] / raiz  # Faz o AB ficar |AB| = 1
    vetor_bspline = (j2[0] - j1[0], j2[1] - j1[1])
    raiz2 = math.sqrt(
        math.pow(vetor_bspline[0], 2) + math.pow(vetor_bspline[1], 2))  # Magnitude do [0,1] do controle da BSPLINE
    bspline.control_points[1] = j1[0] + vetor_bezier_normalizado[0] * raiz2, j1[1] + vetor_bezier_normalizado[1] * raiz2

    # ponto de controle 1 da bspline = Ponto de controle 0 da bspline + ( vetor bezier normalizado * magnitude da bspline )

    print(vetor_bezier_normalizado, vetor_bspline, sep=" | ")

    return [vetor_bezier_normalizado, vetor_bspline]


def draw_c2():
    draw_c0()
    v1, v2 = bezier.control_points[-1], bezier.control_points[-2]  # (x,y), (x,y)
    j1, j2 = bspline.control_points[0], bspline.control_points[1]  # (x,y), (x,y)

    vetor_bezier = (v1[0] - v2[0]), (v1[1] - v2[1])

    bspline.control_points[1] = bspline.control_points[0][0] + vetor_bezier[0], bspline.control_points[0][1] + vetor_bezier[1]


'''

Bezier

'''

bezier = Bezier(control_points=[(486, 252), (191, 103), (481, 57), (703, 190), (704, 366), (497, 582)])

'''

B-spline 

'''

bspline = Bspline(control_points=[])

flag = True
run = True

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if len(bezier.control_points) < 6:
                bezier.control_points.append(event.pos)
            elif len(bspline.control_points) < 9:
                bspline.control_points.append(event.pos)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                print(bezier.control_points, bspline.control_points)
                bezier.control_points.clear()
                bspline.control_points.clear()
                flag = True
            if event.key == pygame.K_b:
                if len(bezier.control_points) == 6 and len(bspline.control_points) == 9:
                    if flag:
                        draw_c0()
                        flag = False
            if event.key == pygame.K_n:
                if len(bezier.control_points) == 6 and len(bspline.control_points) == 9:
                    if flag:
                        draw_c1()
                        flag = False
            if event.key == pygame.K_m:
                if len(bezier.control_points) == 6 and len(bspline.control_points) == 9:
                    if flag:
                        draw_c2()
                        flag = False

    display.fill(0)

    for x, y in bezier.control_points:
        pygame.draw.circle(display, 'pink', (x, y), 5)

    for x, y in bspline.control_points:
        pygame.draw.circle(display, 'pink', (x, y), 5)

    for i in range(len(bezier.control_points) - 1):
        if len(bezier.control_points) >= 2:
            pygame.draw.line(display, "green",
                             start_pos=bezier.control_points[i], end_pos=bezier.control_points[i + 1])

    for i in range(len(bspline.control_points) - 1):
        if len(bspline.control_points) >= 2:
            pygame.draw.line(display, "green",
                             start_pos=bspline.control_points[i], end_pos=bspline.control_points[i + 1])

    if len(bezier.control_points) == 6:
        bezier.draw_bezier(display)

    if len(bspline.control_points) == 9:
        # print(bspline.control_points, bspline.degree, bspline.knots)
        bspline.draw_bspline(display)

    pygame.display.update()

    clock.tick(30)

pygame.quit()
exit()
