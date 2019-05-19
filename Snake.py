import pygame
import random

pygame.init()

pygame.mixer.music.load("Pumping_Irie.wav")
crash_music = pygame.mixer.Sound('Crash.wav')


# Class to Create Buttons
class Button():
    def __init__(self, color, x, y, length, height):
        self.color = color
        self.x = x
        self.y = y
        self.length = length
        self.height = height

        self.rect = pygame.Rect(x, y, length, height)

    def create(self, win):
        pygame.draw.rect(win, self.color, self.rect)


class Snake():

    def __init__(self, xpos, ypos, color, length_head, height_head, win):

        self.xpos = xpos
        self.ypos = ypos
        self.win = win

        self.head = []
        self.body_segments = []

        self.color = color

        self.direction_x = 0
        self.direction_y = 1

        self.length_head = length_head

        self.height_head = height_head

        self.head = pygame.Rect(xpos, ypos, length_head, height_head)

    def create(self):

        pygame.draw.rect(self.win, orange, self.head)


    def movement(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_UP]:

            self.direction_x = 0
            self.direction_y = -1
            self.head.move_ip(0, -5)

        if pressed_key[pygame.K_DOWN]:

            self.direction_x = 0
            self.direction_y = 1
            self.head.move_ip(0, 5)

        if pressed_key[pygame.K_RIGHT]:

            self.direction_x = 1
            self.direction_y = 0
            self.head.move_ip(5, 0)

        if pressed_key[pygame.K_LEFT]:

            self.direction_x = -1
            self.direction_y = 0
            self.head.move_ip(-5, 0)

    def collision(self):

        self.body_segments.append(pygame.draw.rect(self.win, self.color, (self.xpos - self.length_head, self.ypos - self.height_head, self.length_head, self.height_head)))


class DeadEnds():

    def __init__(self, color, x_bound, y_bound, length, height):
        self.color = color

        self.rect = pygame.Rect(x_bound, y_bound, length, height)

    def create_boundary(self, win):

        pygame.draw.rect(win, self.color, self.rect)


class Food():

    def __init__(self, length, height):

        self.length = length
        self.height = height
        self.x_pos = random.randint(15, 855)
        self.y_pos = random.randint(10, 530)
        self.apple = pygame.image.load('apple.png').convert_alpha()
        self.apple = pygame.transform.scale(self.apple, (35, 35))
        self.rect = self.apple.get_rect(topleft=(self.x_pos, self.y_pos))

    def draw_on_screen(self, win):

        win.blit(self.apple, (self.x_pos, self.y_pos))


class Obstacles():

    def __init__(self, x_pos, y_pos, length, height):

        self.x_pos = x_pos
        self.y_pos = y_pos
        self.length = length
        self.height = height
        self.hawk = pygame.image.load('hawk.png').convert_alpha()
        self.hawk = pygame.transform.scale(self.hawk, (65, 65))
        self.rect = self.hawk.get_rect(topleft=(x_pos, y_pos))

        self.rect = pygame.Rect(x_pos, y_pos, length, height)

    def screen(self, win):
        win.blit(self.hawk, (self.x_pos, self.y_pos))


font = pygame.font.SysFont(None, 72)
window_intro = pygame.display.set_mode((900, 450))
window_background = pygame.image.load('background.png')
window_background = pygame.transform.scale(window_background, (900, 600))
window_game = pygame.display.set_mode((900, 600))
window_end = pygame.display.set_mode((900, 600))


pygame.display.set_caption('Snake Reloaded')
white = (255, 255, 255)
menu_color = (238, 223, 204)
black = (0, 0, 0)
orange = (238, 118, 0)
green = (0, 128, 0)
red = (255, 0, 0)

clock = pygame.time.Clock()

level_1 = Button(orange, 10, 10, 200, 50)
level_2 = Button(orange, 650, 10, 200, 50)
level_3 = Button(orange, 10, 450, 200, 50)


snake_obj = Snake(100, 75, green, 25, 20, window_game)

food = [Food(35, 35)]

boundary_1 = DeadEnds(green, 0, 0, 900, 5)
boundary_2 = DeadEnds(green, 0, 0, 5, 600)
boundary_3 = DeadEnds(green, 0, 595, 830, 5)
boundary_4 = DeadEnds(green, 895, 0, 5, 600)

edges = [boundary_1, boundary_2, boundary_3, boundary_4]


# Calls a function to add messages to Screen
def message_to_screen(msg, color, horizontal, vertical, win):
    text_screen = font.render(msg, True, color)
    win.blit(text_screen, [horizontal, vertical])


# Creates Game Loop


def game_loop(win):

    crashed = False
   # pygame.mixer.music.play(-1)

    x_pos = 0
    y_pos = 0
    length = 0
    height = 0
    list_hawks_x = []
    list_hawks_y = []

    if level_1.rect.collidepoint(pos):
        for j in range(0, 2):
            x_pos = random.randint(25, 860)
            y_pos = random.randint(-8, -3)
            length = 30
            height = 30
            speed_y = 10
            speed_x = 10
            list_hawks_x.append(x_pos)
            list_hawks_y.append(y_pos)
    elif level_2.rect.collidepoint(pos):
        for j in range(0, 4):
            x_pos = random.randint(25, 860)
            y_pos = random.randint(-8, -3)
            length = 30
            height = 30
            speed_y = 12
            speed_x = 12
            list_hawks_x.append(x_pos)
            list_hawks_y.append(y_pos)
    elif level_3.rect.collidepoint(pos):
        for j in range(0, 6):
            x_pos = random.randint(25, 860)
            y_pos = random.randint(-8, -3)
            length = 30
            height = 30
            speed_y = 14
            speed_x = 14
            list_hawks_x.append(x_pos)
            list_hawks_y.append(y_pos)

    while not crashed:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

        win.fill(menu_color)
        win.blit(window_background, (0, 0))

        snake_obj.create()

        snake_obj.movement()

        hawk_vertical = len(list_hawks_x) / 2
        hawk_horizontal = len(list_hawks_x) / 2

        for i in range(0, int(hawk_vertical)):

            list_hawks_y[i] = list_hawks_y[i] + speed_y
            hawk = Obstacles(list_hawks_x[i], list_hawks_y[i], length, height)
            hawk.screen(win)
            if list_hawks_y[i] > 600:
                list_hawks_y[i] = 0 - height
                list_hawks_x[i] = random.randint(45, 850)
            if snake_obj.head.colliderect(hawk.rect):
                pygame.mixer_music.stop()
                pygame.mixer.Sound.play(crash_music)
                game_over_screen(window_end)

        for j in range(int(hawk_vertical), len(list_hawks_x)):
            list_hawks_x[j] = list_hawks_x[j] + speed_x
            hawk_2 = Obstacles(list_hawks_x[j], list_hawks_y[j], length, height)
            hawk_2.screen(win)
            if list_hawks_x[j] > 900:
                list_hawks_x[j] = 0 - height
                list_hawks_y[j] = random.randint(35, 530)
            if snake_obj.head.colliderect(hawk_2.rect):
                pygame.mixer_music.stop()
                pygame.mixer.Sound.play(crash_music)
                game_over_screen(window_end)

        for i in range(0, len(edges)):
            edges[i].create_boundary(win)
            if snake_obj.head.colliderect(edges[i]):
                pygame.mixer_music.stop()
                pygame.mixer.Sound.play(crash_music)
                game_over_screen(window_end)

        for food_num in food:
            food_num.draw_on_screen(win)
            if snake_obj.head.colliderect(food_num.rect):
                snake_obj.collision()
                food.remove(food_num)
                food.append(Food(35, 35))
                food_num.draw_on_screen(win)

        pygame.display.update()
        clock.tick(60)


def game_over_screen(win):

    end = True
    pygame.mixer_music.play(-1)

    while end:
        message_to_screen('Sorry Game Over Try Again', black, 40, 250, window_end)
        message_to_screen('Enter S to Start Over', black, 50, 450, window_end)
        pygame.display.update()
        for events in pygame.event.get():
            values = pygame.key.get_pressed()
            if events.type == pygame.QUIT:
                end = False
                pygame.quit()
                quit()

        pygame.display.update()
        win.fill(menu_color)
        clock.tick(60)


intro = True
   # pygame.mixer_music.play(-1)

while intro:

    level_1.create(window_intro)
    level_2.create(window_intro)
    level_3.create(window_intro)
    message_to_screen('Level 1', black, 18, 15,  window_intro)
    message_to_screen('Level 2', black, 658, 15, window_intro)
    message_to_screen('Level 3', black, 15, 451, window_intro)
    message_to_screen('WELCOME TO SNAKE RELOADED', black, 40, 250, window_intro)
    pygame.display.update()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            intro = False
            pygame.quit()
            quit()

        if e.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if level_1.rect.collidepoint(pos):
                game_loop(window_intro)

            elif level_2.rect.collidepoint(pos):
                game_loop(window_intro)

            elif level_3.rect.collidepoint(pos):
                game_loop(window_intro)

    window_intro.fill(menu_color)
    clock.tick(60)

game_loop(window_game)
game_over_screen(window_end)
pygame.quit()
quit()







