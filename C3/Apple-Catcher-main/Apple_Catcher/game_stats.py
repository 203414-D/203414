class GameStats:
    # estadisiticas del juego
    def __init__(self, ac_game):
        self.settings = ac_game.settings
        self.game_active = False
        self.reset_stats()

    def reset_stats(self):
        self.apples_left = self.settings.apple_limit
        self.gapples_left = self.settings.gapple_limit
        self.score = 0
        self.level = 1