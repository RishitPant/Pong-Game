# Ping Pong Game with Pygame!!
# coding:cp1252
#Credits: @RishitPant - GitHub

import pygame
import sys
import random


# ---------------Initialise Pygame--------------
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
clock = pygame.time.Clock()

# -----------Main Window Setup------------------#
screen_width = 1250   #Can chnage to W: 1280 H:960
screen_heigth = 700
screen = pygame.display.set_mode((screen_width, screen_heigth))
icon = pygame.image.load("icon_107.png")
ready_text = pygame.image.load("start_image.png")
pygame.display.set_caption("Ping Pong Game")
pygame.display.set_icon(icon)


# ----------Game Units-------------------#
ball = pygame.Rect(screen_width//2 - 15, screen_heigth//2 - 15, 30, 30)
player = pygame.Rect(screen_width - 24, screen_heigth//2 - 70, 19, 140)
opponent = pygame.Rect(6, screen_heigth//2 - 70, 19, 140)


#-----------Background-------------------#
bg_color = pygame.Color("grey12")
light_grey = (200, 200, 200)


# ============Controlling Ball And Player movement============#


def ball_control():
    global ball_speed_x, ball_speed_y, score_player, score_opponent, time

    # ================== Ball Movement =============#
    
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Reversing the ball to bounce when hit to the boundary------------

    if ball.top <= 0 or ball.bottom >= screen_heigth:
        pygame.mixer.Sound.play(pong_sound)
        ball_speed_y *= -1

    if ball.left <= 0:
        pygame.mixer.Sound.play(score_sound)
        score_player += 1
        time = pygame.time.get_ticks()

    if ball.right >= screen_width:
        pygame.mixer.Sound.play(score_sound)
        score_opponent += 1
        time = pygame.time.get_ticks()

    if ball.colliderect(player) or ball.colliderect(opponent):
        pygame.mixer.Sound.play(pong_sound)
        ball_speed_x *= -1


def player_control():
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_heigth:
        player.bottom = screen_heigth

def opponent_controls():
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_heigth:
        opponent.bottom = screen_heigth

"""def opponent_control():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_heigth:
        opponent.bottom = screen_heigth"""

def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])


def ball_position():
    global ball_speed_y, ball_speed_x, time

    current_time = pygame.time.get_ticks()
    ball.center = (screen_width//2, screen_heigth//2)

    if current_time - time < 700:
        number_three = font.render("3", False, light_grey)
        screen.blit(number_three, (screen_width//2 - 10, screen_heigth//2 + 20))
    if 700 < current_time - time < 1400:
        number_two = font.render("2", False, light_grey)
        screen.blit(number_two, (screen_width//2 - 10, screen_heigth//2 + 20))
    if 1400 < current_time - time < 2100:
        number_one = font.render("1", False, light_grey)
        screen.blit(number_one, (screen_width//2 - 10, screen_heigth//2 + 20))

    if current_time - time < 2100:
        ball_speed_x, ball_speed_y = 0, 0
    else:
        ball_speed_y = 10 * random.choice((1, -1))
        ball_speed_x = 10 * random.choice((1, -1))
        time = None

# Display player score


def font_player():
    player_font = font.render(f"{score_player}", False, light_grey)
    screen.blit(player_font, (653, 340))

# Diplay opponent score


def font_opponent():
    opponent_font = font.render(f"{score_opponent}", False, light_grey)
    screen.blit(opponent_font, (580, 340))

# Graphical user interface




def main_game():
    global player_speed, opponent_speed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 6
            if event.key == pygame.K_UP:
                player_speed -= 6
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed += 6
            if event.key == pygame.K_UP:
                player_speed -= 6


# Controls For 1v1 Human Vs Human --------------
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                opponent_speed += 6
            if event.key == pygame.K_w:
                opponent_speed -= 6
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                opponent_speed += 6
            if event.key == pygame.K_w:
                opponent_speed -= 6

    #Screen Draw
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 255 ,0), player)
    pygame.draw.rect(screen, (255, 0, 0), opponent)
    pygame.draw.ellipse(screen, (255, 255, 0), ball)
    pygame.draw.aaline(screen, light_grey, (screen_width//2, 0),(screen_width//2, screen_heigth))


    #Control ball movement
    ball_control()

    player.y += player_speed
    opponent.y += opponent_speed

    #Controls player movement
    player_control()

    #Controls opponent Movement, score
    opponent_controls()


    #Making Surface with font text, for player
    font_player()

    #Timer Function
    if time:
        ball_position()

    #Oponents surface for opponent score
    font_opponent()


    #-------Update the game window--------
    pygame.display.flip()

def state_manager(self):
    if self.state == 'intro':
        self.intro()
    if self.state == 'main_game':
        self.main_game()

#Calling GameState Class


#Speed of ball is defined
ball_speed_x = 10 * random.choice((1, -1))#Testing at 12. Expected at 7.
ball_speed_y = 10 * random.choice((1, -1))


#Player and Opponent Speed VAriables
player_speed = 0
opponent_speed = 0

#Score Variables
score_player = 0
score_opponent = 0
font = pygame.font.Font("freesansbold.ttf", 32)

#Timer Function
time = True

#Sounds In-Game
pong_sound = pygame.mixer.Sound("sound22.ogg")
score_sound = pygame.mixer.Sound("sound23.ogg")


#=================== Main Game Loop ====================#
while True:
    main_game()
    clock.tick(60)