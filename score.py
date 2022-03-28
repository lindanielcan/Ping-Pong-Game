import pygame


class Score:
    def __init__(self, screen, setting):
        # Three rect needed.
        # rect one: player one label on the screen
        # rect two: player two label on the screen
        # rect three: score label

        self.screen = screen
        self.setting = setting
        self.text_file = 'FreeSansBold.ttf'

        self.player_one_label_font = pygame.font.Font(self.text_file, 15)
        self.player_two_label_font = pygame.font.Font(self.text_file, 15)
        self.score_label_font = pygame.font.Font(self.text_file, 15)
        self.game_over_label_font = pygame.font.Font(self.text_file, 15)

        self.player_one_score = 0
        self.player_two_score = 0

        self.player_one_label_text = self.player_one_label_font.render('Player One', True, 'white', 'black')
        self.player_two_label_text = self.player_two_label_font.render('Player Two', True, 'white', 'black')
        self.score_label_text = self.score_label_font.render(f'{self.player_one_score} - {self.player_two_score}', True,
                                                             'white', 'black')
        self.game_over_label_text = self.game_over_label_font.render('Game Over', True, 'white', 'black')

        self.player_one_label_rect = self.player_one_label_text.get_rect()
        self.player_two_label_rect = self.player_two_label_text.get_rect()
        self.score_label_rect = self.score_label_text.get_rect()
        self.game_over_label_rect = self.score_label_text.get_rect()

        self.player_one_label_rect.center = (50, 10)
        self.player_two_label_rect.center = (self.setting.screen_width - 50, 10)
        self.score_label_rect.center = (self.setting.screen_width / 2, 10)

    def show_score(self):
        self.score_label_text = self.score_label_font.render(f'{self.player_one_score} - {self.player_two_score}', True,
                                                             'white', 'black')
        self.screen.blit(self.score_label_text, self.score_label_rect)

    def show_player_label(self):

        self.screen.blit(self.player_one_label_text, self.player_one_label_rect)
        self.screen.blit(self.player_two_label_text, self.player_two_label_rect)

    def show_game_over_label(self, who_won):

        self.game_over_label_rect.center = (self.setting.screen_width / 2 - 50, self.setting.screen_height / 2)

        if who_won == 'player_one':

            self.game_over_label_text = self.game_over_label_font.render(
                'Player One Won', True,
                'white', 'black')

        elif who_won == 'player_two':

            self.game_over_label_text = self.game_over_label_font.render(
                'Player Two Won', True,
                'white', 'black')

        self.screen.blit(self.game_over_label_text, self.game_over_label_rect)
