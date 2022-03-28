import pygame
from setting import Setting


class Paddle:
    def __init__(self, screen, x_cor, y_cor):
        self.screen = screen
        self.setting = Setting()
        self.paddle_width = 30
        self.paddle_height = 100
        self.paddle = pygame.transform.scale(pygame.image.load('images/rectangle.png'),
                                             (self.paddle_width, self.paddle_height)).convert_alpha(screen)
        self.x_cor = x_cor
        self.y_cor = y_cor

        self.paddle_rect = self.paddle.get_rect(center=(self.x_cor, self.y_cor))

        self.paddle_speed = 0.1

        # print(self.paddle_rect.top," ", self.paddle_rect.bottom," ", self.paddle_rect.left, ", ")

    def draw_paddle(self):
        self.paddle_rect = self.paddle.get_rect(center=(self.x_cor, self.y_cor))
        self.screen.blit(self.paddle, self.paddle_rect)

    def move_paddle(self, move_up, move_down):
        """Moves paddle as long as it does not go out the screen."""
        if self.y_cor >= (self.paddle_height / 2):
            if move_up:
                self.move_paddle_up()
        if self.y_cor <= (self.setting.screen_height - (self.paddle_height / 2)):
            if move_down:
                self.move_paddle_down()

    def move_paddle_up(self):
        self.y_cor -= self.paddle_speed

    def move_paddle_down(self):
        self.y_cor += self.paddle_speed
