# # import pygame module in this program
# import pygame
#
# # activate the pygame library .
# # initiate pygame and give permission
# # to use pygame's functionality.
# pygame.init()
#
# # create the display surface object
# # of specific dimension..e(500, 500).
# win = pygame.display.set_mode((500, 500))
#
# # set the pygame window name
# pygame.display.set_caption("Moving rectangle")
#
# # object current co-ordinates
# x = 200
# y = 200
#
# # dimensions of the object
# width = 20
# height = 20
#
# # velocity / speed of movement
# vel = 10
#
# # Indicates pygame is running
# run = True
#
# # infinite loop
# while run:
#     # creates time delay of 10ms
#     pygame.time.delay(10)
#
#     # iterate over the list of Event objects
#     # that was returned by pygame.event.get() method.
#     for event in pygame.event.get():
#
#         # if event object type is QUIT
#         # then quitting the pygame
#         # and program both.
#         if event.type == pygame.QUIT:
#             # it will make exit the while loop
#             run = False
#     # stores keys pressed
#     keys = pygame.key.get_pressed()
#
#     # if left arrow key is pressed
#     if keys[pygame.K_LEFT] and x > 0:
#         # decrement in x co-ordinate
#         x -= vel
#
#     # if left arrow key is pressed
#     if keys[pygame.K_RIGHT] and x < 500 - width:
#         # increment in x co-ordinate
#         x += vel
#
#     # if left arrow key is pressed
#     if keys[pygame.K_UP] and y > 0:
#         # decrement in y co-ordinate
#         y -= vel
#
#     # if left arrow key is pressed
#     if keys[pygame.K_DOWN] and y < 500 - height:
#         # increment in y co-ordinate
#         y += vel
#
#     # completely fill the surface object
#     # with black colour
#     win.fill((0, 0, 0))
#
#     # drawing object on screen which is rectangle here
#     pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
#
#     # it refreshes the window
#     pygame.display.update()
#
# # closes the pygame window
# pygame.quit()


import pygame

# --- constants --- (UPPER_CASE names)

SCREEN_WIDTH = 430
SCREEN_HEIGHT = 410

#BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)

FPS = 30

# --- classses --- (CamelCase names)

# empty

# --- functions --- (lower_case names)

# empty

# --- main ---

# - init -

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#screen_rect = screen.get_rect()

pygame.display.set_caption("Tracking System")

# - objects -

rectangle = pygame.rect.Rect(176, 134, 17, 17)
rectangle_draging = False

# - mainloop -

clock = pygame.time.Clock()

running = True

while running:

    # - events -

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if rectangle.collidepoint(event.pos):
                    rectangle_draging = True
                    mouse_x, mouse_y = event.pos
                    offset_x = rectangle.x - mouse_x
                    offset_y = rectangle.y - mouse_y

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                rectangle_draging = False

        elif event.type == pygame.MOUSEMOTION:
            if rectangle_draging:
                mouse_x, mouse_y = event.pos
                rectangle.x = mouse_x + offset_x
                rectangle.y = mouse_y + offset_y

    # - updates (without draws) -

    # empty

    # - draws (without updates) -

    screen.fill(WHITE)

    pygame.draw.rect(screen, RED, rectangle)

    pygame.display.flip()

    # - constant game speed / FPS -

    clock.tick(FPS)

# - end -

pygame.quit()