import pygame
from Bspline import Bspline
from Bezier import Bezier

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

    draw_c1()

    print(f' {bezier.control_points} {bspline.control_points} {coef_x, coef_y}')


def draw_c1():
    v1,v2 = bezier.control_points[-1], bezier.control_points[-2]
    j1,j2 = bspline.control_points[1], bspline.control_points[2]

    vetor_bezier, vetor_bspline = (abs(v2[0] - v1[0]), abs(v2[1] - v1[1])), (abs(j1[0] - j2[0]), abs(j1[1] - j2[1]))

    print(vetor_bezier, vetor_bspline, sep=" | ")

    return [vetor_bezier,vetor_bspline]

'''

Bezier

'''

bezier = Bezier(control_points=[(84, 229), (163, 148), (205, 202), (319, 111), (392, 211), (317, 297)] )

'''

B-spline 

'''


bspline = Bspline(control_points=[(317, 297), (241, 393), (385, 465), (464, 396), (611, 527), (510, 699), (321, 769), (273, 641), (371, 547)])

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
