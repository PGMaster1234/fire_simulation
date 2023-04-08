import pygame
import random

screen = pygame.display.set_mode((1200, 650))
smoke_surface = pygame.Surface((1200, 650))

clock = pygame.time.Clock()

pygame.init()
font15 = pygame.font.Font("freesansbold.ttf", 15)

fire_particles = []
wood_blocks = []
ground = 580
smoke_particles = []

fire_pit = pygame.Rect(400, 580, 400, 25)

running = True
while running:

    screen.fill((200, 200, 200))
    smoke_surface.fill((100, 100, 100))
    pygame.draw.ellipse(screen, (0, 0, 0), fire_pit, 20)

    mx, my = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            wood_blocks.append([pygame.Rect(mx - 50, my, 100, 20), random.randint(-5, -3)])

    for block in wood_blocks:
        block[1] += 0.3
        if block[0].y < ground:
            block[0].y += block[1]
        if block[0].y > (ground - 10):
            block[0].y = ground
        if block[0].height < 1:
            wood_blocks.remove(block)

        pygame.draw.rect(screen, (54, 38, 36), block[0], 0)

        if block[0].y > 570:
            if random.randint(1, 15) == 1:
                block[0].width -= 0.5
                block[0].x += 0.5
                block[0].height -= 0.0001
            if block[0].colliderect(fire_pit):
                for i in range(10):
                    fire_particles.append([[block[0].x + random.randint(0, 100),  # 01 - X
                                            random.randint(575, 600)],  # 02 - Y
                                           random.uniform(4, 6),  # 1 - Vel up
                                           random.uniform(-3, 3),  # 2 Turbulence
                                           random.randint(7, 10),  # 3 Radius
                                           random.uniform(0.1, 0.5),  # 4 Particle burn out
                                           random.randint(150, 190),  # 5 Amount of red
                                           random.uniform(-2, 2)])  # 6 Curve down

    for fp in fire_particles:
        fp[0][1] -= fp[1]
        fp[3] -= fp[4]
        fp[5] -= fp[5] / 25

        fp[0][0] -= fp[2]
        fp[0][1] += fp[6]

        if fp[3] < 3:
            fire_particles.remove(fp)
            if random.randint(0, 50) == 1:
                smoke_particles.append([fp[0][0], fp[0][1] - 50, 10])

        pygame.draw.circle(screen, (240, fp[5], 0), (fp[0][0], fp[0][1]), fp[3])

    for smoke in smoke_particles:
        pygame.draw.circle(smoke_surface, (0, 0, 0), (smoke[0], smoke[1]), smoke[2])
        smoke[2] += 0.1
        smoke[1] -= 2
        if smoke[2] > 30:
            smoke_particles.remove(smoke)

    # ------------- Show fps
    fps = clock.get_fps()
    fps_string = str(fps)
    screen.blit(font15.render(fps_string, True, (255, 255, 255)), (1000, 500))

    smoke_surface.set_alpha(50)
    screen.blit(smoke_surface, (0, 0))
    pygame.display.update()
    clock.tick(60)

# for check in fire_particles:
#    if abs(check[0][0] - fp[0][0]) < 50:
#        if abs(check[0][1] - fp[0][1]) < 50:
#            fp[2] -= check[2] / 100
#            if check[6] < fp[6]:
#                fp[6] -= 0.01
#            else:
#                fp[6] += 0.01
