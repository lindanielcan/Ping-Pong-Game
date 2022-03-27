import pygame, sys
from ball import Ball
from paddle import Paddle
from score import Score
from setting import Setting


class Game:
    def __init__(self):
        # initialize pygame
        pygame.init()
        self.setting = Setting()
        self.screen = pygame.display.set_mode(self.setting.screen_size)
        self.ball = Ball(self.screen, self.setting.screen_width/2, self.setting.screen_height/2)
        self.player_one = Paddle(self.screen, 15, 50)
        self.player_two = Paddle(self.screen, 585, 200)

        self.player_one_move_up = False
        self.player_one_move_down = False
        self.player_two_move_up = False
        self.player_two_move_down = False

    def run(self):

        # Listen for key events.
        while True:

            # Fill background.
            self.screen.fill(self.setting.back_ground_color)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.player_one_move_up = True
                    elif event.key == pygame.K_s:
                        self.player_one_move_down = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        self.player_one_move_up = False
                    elif event.key == pygame.K_s:
                        self.player_one_move_down = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.player_two_move_up = True
                    elif event.key == pygame.K_DOWN:
                        self.player_two_move_down = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.player_two_move_up = False
                    elif event.key == pygame.K_DOWN:
                        self.player_two_move_down = False

            # Make sure the paddles don't go over the screen
            if self.player_one.y_cor >= 50:
                if self.player_one_move_up:
                    self.player_one.move_paddle_up()
            if self.player_one.y_cor <= 350:
                if self.player_one_move_down:
                    self.player_one.move_paddle_down()
            if self.player_two.y_cor >= 50:
                if self.player_two_move_up:
                    self.player_two.move_paddle_up()
            if self.player_two.y_cor <= 350:
                if self.player_two_move_down:
                    self.player_two.move_paddle_down()

            # Draw two paddles.
            self.player_one.draw_paddle()
            self.player_two.draw_paddle()

            # Draw ball
            self.ball.draw_ball()

            pygame.display.update()
