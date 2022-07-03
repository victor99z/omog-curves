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

    print(f' {bezier.control_points} - {bspline.control_points} - {coef_x, coef_y}')

    for i in range(len(bspline.control_points)):
        x, y = bspline.control_points[i]
        bspline.control_points[i] = (x + coef_x, y + coef_y)


'''

Bezier

'''

pos_list1 = [(104, 176), (164, 111), (241, 184), (284, 103), (339, 193), (470, 123)]  # Bezier

bezier = Bezier(control_points=pos_list1)

'''

B-spline 

'''

points = []

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
            else:
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

    if len(bspline.control_points) > 9:
        print(bspline.control_points, bspline.degree, bspline.knots)
        bspline.draw_bspline(display)

    pygame.display.update()

    clock.tick(30)

pygame.quit()
exit()
