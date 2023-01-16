# 1) Создайте программу для игры с конфетами человек против бота.
# Условие задачи: На столе лежит 120 конфет. Играют
# два игрока делая ход друг после друга. Первый ход делает человек.
# За один ход можно забрать не более чем 28 конфет.
# Победитель - тот, кто оставил на столе 0 конфет.
# 1) Создайте программу для игры с конфетами человек против бота.
# Условие задачи: На столе лежит 120 конфет. Играют
# два игрока делая ход друг после друга. Первый ход делает человек.
# За один ход можно забрать не более чем 28 конфет.
# Победитель - тот, кто оставил на столе 0 конфет.

from random import randint as ri

TOTAL_SWEETS: int = 120
PLAYER_SWEETS: int = 0
BOT_SWEETS: int = 0
SWEETS_PER_MOVE: int = 28


class Game:
    NUMBER_OF_TURN: int = ri(1, 2)

    def __init__(self,
                 total_sweets: int,
                 player_sweets: int,
                 bot_sweets: int,
                 take_sweets) -> int:

        self.total_sweets = total_sweets
        self.player_sweets = player_sweets
        self.bot_sweets = bot_sweets
        self.take_sweets = take_sweets

    def who_is_first(self) -> None:
        """Определяет чей ход будет первым"""
        if self.NUMBER_OF_TURN == 1:
            print(f'Вы начинаете первым! На столе '
                  f' {self.total_sweets} конфет')
            return self.player_turn()
        else:
            print('Бот начинает первым')
            self.bot_turn()

    def player_turn(self) -> str:
        """Возвращает количество взятых Игроком конфет"""

        take_sweets = int(input('Введите количество конфет, '
                                'которое хотите взять, '
                                'но НЕ БОЛЕЕ 28 конфет: '))

        while (take_sweets > SWEETS_PER_MOVE
               or take_sweets < 28
               or take_sweets > self.total_sweets):
            take_sweets: int = int(input('Соблюдайте условия игры! '
                                         'Введите верное количество '
                                         'конфет: '))
        self.total_sweets -= take_sweets
        self.player_sweets += take_sweets

        if self.total_sweets > 0:
            self.bot_turn()
        else:
            print('Вы выиграли, поздравляем!')

    def bot_turn(self) -> str:
        """Возвращает информацио о количестве взятых ботом конфет"""
        take_sweet: int = (self.total_sweets % 29
                           if self.total_sweets != 0
                           else ri(1, 28))
        self.total_sweets -= take_sweet
        self.bot_sweets += take_sweet
        print(f'Бот взял {self.take_sweets} конфет, '
              f'на столе осталось '
              f'{self.total_sweets} конфет!')

        if self.total_sweets > 0:
            self.player_turn()
        else:
            print('Бот победил!')

    def start_game(self) -> str:
        """Информационное сообщение о правилах игры"""
        print(f'На столе лежит {TOTAL_SWEETS} конфет.'
              f'Играют два игрока делая ход друг после друга. '
              f'Первый ход делает человек.\nЗа один ход можно '
              f'забрать не более чем {SWEETS_PER_MOVE} конфет. '
              f'Победитель - тот, кто оставил на столе 0 конфет.')
        print()
        return self.who_is_first()


game_start = Game(TOTAL_SWEETS, PLAYER_SWEETS, BOT_SWEETS, SWEETS_PER_MOVE)
game_start.start_game()
