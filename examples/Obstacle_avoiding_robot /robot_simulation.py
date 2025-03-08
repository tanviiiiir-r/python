import pygame
import numpy as np

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Obstacle Avoiding Robot Simulation")

robot_pos = np.array([300.0, 300.0])
robot_angle = 50
speed = 10
sensor_range = 50

obstacles = [
    (100, 200, 20), (400, 400, 30), (250, 450, 25),
    (500, 100, 20), (150, 500, 30), (350, 150, 25),
    (450, 250, 20), (50, 50, 15)
]

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

def detect_obstacle(robot_pos, angle):
    for (ox, oy, radius) in obstacles:
        distance = np.linalg.norm(robot_pos - np.array([ox, oy]))
        if distance < sensor_range + radius:
            return True
    return False

def check_free_space(robot_pos, robot_angle):
    forward_direction = np.array([np.cos(np.radians(robot_angle)), np.sin(np.radians(robot_angle))])
    forward_pos = robot_pos + forward_direction * sensor_range

    left_direction = np.array([np.cos(np.radians(robot_angle - 90)), np.sin(np.radians(robot_angle - 90))])
    left_pos = robot_pos + left_direction * sensor_range

    right_direction = np.array([np.cos(np.radians(robot_angle + 90)), np.sin(np.radians(robot_angle + 90))])
    right_pos = robot_pos + right_direction * sensor_range

    return forward_pos, left_pos, right_pos

def check_boundaries(robot_pos):
    if robot_pos[0] <= 0 or robot_pos[0] >= 600 or robot_pos[1] <= 0 or robot_pos[1] >= 600:
        return True
    return False

def bounce_mirror(robot_angle, robot_pos):
    if robot_pos[0] <= 0 or robot_pos[0] >= 600:
        robot_angle = 180 - robot_angle
    if robot_pos[1] <= 0 or robot_pos[1] >= 600:
        robot_angle = -robot_angle
    return robot_angle

running = True
while running:
    screen.fill(WHITE)

    pygame.draw.circle(screen, BLUE, robot_pos.astype(int), 10)
    for (ox, oy, radius) in obstacles:
        pygame.draw.circle(screen, RED, (ox, oy), radius)

    if detect_obstacle(robot_pos, robot_angle):
        forward_pos, left_pos, right_pos = check_free_space(robot_pos, robot_angle)

        if not detect_obstacle(left_pos, robot_angle):
            robot_angle -= 90
        elif not detect_obstacle(right_pos, robot_angle):
            robot_angle += 90
        else:
            robot_angle += 180

    robot_pos += speed * np.array([np.cos(np.radians(robot_angle)), np.sin(np.radians(robot_angle))])

    if check_boundaries(robot_pos):
        robot_angle = bounce_mirror(robot_angle, robot_pos)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    pygame.time.delay(100)

pygame.quit()
