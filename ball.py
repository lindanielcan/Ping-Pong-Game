import random
import pygame.image
from random import randint


class Ball:
    def __init__(self, screen, setting):
        self.screen = screen
        self.ball_radius = 20
        self.setting = setting
        self.x_cor = self.setting.screen_width / 2
        self.y_cor = self.setting.screen_height / 2
        self.ball = pygame.transform.scale(pygame.image.load('images/ball.png', ),
                                           (self.ball_radius, self.ball_radius)).convert_alpha(self.screen)
        self.ball_rect = self.ball.get_rect(center=(self.x_cor, self.y_cor))

        self.ball_speed = 0.03

        self.ball_speed_x = self.ball_speed
        self.ball_speed_y = self.ball_speed

        # Initialize which quadrant that the ball is gonna go.
        self.quadrants = random.randint(1, 4)

        self.wall_hit = False
        self.paddle_hit = False

    def draw_ball(self):
        self.ball_rect = self.ball.get_rect(center=(self.x_cor, self.y_cor))
        self.screen.blit(self.ball, self.ball_rect)

    def move_ball(self):

        self.set_direction()

        self.ball_hit_wall()

        self.ball_rect = self.ball.get_rect(center=(self.x_cor, self.y_cor))

    def set_direction(self):
        """Change the direction of the ball movement, and move the ball"""

        if self.quadrants == 1:
            self.x_cor += self.ball_speed_x
            self.y_cor -= self.ball_speed_y
        elif self.quadrants == 2:
            self.x_cor -= self.ball_speed_x
            self.y_cor -= self.ball_speed_y
        elif self.quadrants == 3:
            self.x_cor -= self.ball_speed_x
            self.y_cor += self.ball_speed_y
        elif self.quadrants == 4:
            self.x_cor += self.ball_speed_x
            self.y_cor += self.ball_speed_y

    def ball_hit_paddle(self, paddle_rect, player_name):
        """Ball should turn direction with it is hit by the paddle."""

        if player_name == 'player_one':
            if paddle_rect.top <= self.ball_rect.centery <= paddle_rect.bottom \
                    and self.ball_rect.left + 15 <= paddle_rect.right:
                if self.quadrants == 2:
                    self.quadrants = 1
                elif self.quadrants == 3:
                    self.quadrants = 4
        elif player_name == 'player_two':
            if paddle_rect.top <= self.ball_rect.centery <= paddle_rect.bottom \
                    and self.ball_rect.right - 15 >= paddle_rect.left:
                if self.quadrants == 1:
                    self.quadrants = 2
                elif self.quadrants == 4:
                    self.quadrants = 3

    def ball_hit_wall(self):
        """If the ball hits the wall, turn its direction."""
        if self.y_cor <= (self.ball_radius / 2):
            if self.quadrants == 1:
                self.quadrants = 4
            elif self.quadrants == 2:
                self.quadrants = 3
        elif self.y_cor >= (self.setting.screen_height - (self.ball_radius / 2)):
            if self.quadrants == 3:
                self.quadrants = 2
            elif self.quadrants == 4:
                self.quadrants = 1

    def ball_pass_left_or_right_screen(self):

        if self.ball_rect.centerx <= 0:
            self.x_cor = self.setting.screen_width / 2
            self.y_cor = self.setting.screen_height / 2
            self.quadrants = random.randint(1, 4)
            return 0
        elif self.ball_rect.centerx >= self.setting.screen_width:
            self.x_cor = self.setting.screen_width / 2
            self.y_cor = self.setting.screen_height / 2
            self.quadrants = random.randint(1, 4)
            return 1
