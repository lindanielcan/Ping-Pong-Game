import pygame.image


class Ball:
    def __init__(self, screen, x_cor, y_cor):
        self.screen = screen
        self.ball_radius = 100

        self.x_cor = x_cor
        self.y_cor = y_cor
        self.ball = pygame.transform.scale(pygame.image.load('images/football.png', ),
                                           (self.ball_radius, self.ball_radius)).convert_alpha(self.screen)
        self.ball_rect = self.ball.get_rect(center=(self.x_cor, self.y_cor))

    def draw_ball(self):
        self.screen.blit(self.ball, self.ball_rect)