import numpy as np


class Nonograma:
    def __init__(self, n):
        self.player_board = np.zeros((n, n), dtype=int)
        self.sol_board = np.zeros((n, n), dtype=int)

    def get_sol(self):
        return self.sol_board

    def get_player(self):
        return self.player_board

    def set_sol(self, m_sol):
        return

    def set_player(self, save):
        return

    def win_condition(self):
        return

    def load_level(self, level):
        return