import pygame


class Paddle:
    def __init__(self, screen, x_cor, y_cor):
        self.screen = screen
        self.paddle_width = 30
        self.paddle_height = 100
        self.paddle = pygame.transform.scale(pygame.image.load('images/rectangle.png'),
                                             (self.paddle_width, self.paddle_height)).convert_alpha(screen)
        self.x_cor = x_cor
        self.y_cor = y_cor

        self.paddle_rect = self.paddle.get_rect(center=(self.x_cor, self.y_cor))

        self.paddle_speed = 0.01

    def draw_paddle(self):
        self.paddle_rect = self.paddle.get_rect(center=(self.x_cor, self.y_cor))
        self.screen.blit(self.paddle, self.paddle_rect)

    def move_paddle_up(self):
        self.y_cor -= self.paddle_speed

    def move_paddle_down(self):
        self.y_cor += self.paddle_speed
