COUNTER = 0
COUNTER1 = 8
VALUES = list(range(1,10))

class GameBoard:
    SEPARATOR = '|'
    LINE = '-'
    SQUARE_SIZE = 3
    LINE_SIZE = 13
    
    def __init__(self,
                board_data: list):       
        self.board_data = board_data

    def draw_board(self) -> str:
        """Возвращает поле для игры"""
        print(self.LINE * self.LINE_SIZE)
        for sep in range(self.SQUARE_SIZE):
            print(self.SEPARATOR, 
                  self.board_data[0 + sep * 3],
                  self.SEPARATOR, 
                  self.board_data[1 + sep * 3],
                  self.SEPARATOR, 
                  self.board_data[2 + sep * 3],
                  self.SEPARATOR)
        print(self.LINE * self.LINE_SIZE)

game = GameBoard(list(range(1,10)))
game.draw_board()
    

class Game(GameBoard):
    def __init__(self,
                 board_data: list,
                 player_token: str):
        super().__init__(self, board_data)
        self.board_data = board_data
        self.player_token = player_token

    def input_values(self) -> str:
        while True:
            value = input('Выберети яичейку: ' + self.player_token)
            if not(value in '123456789'):
                print('Ошибка ввода! Выберете яичейку от 1 до 9!')
                continue
            value = int(value)
            if str(self.board_data[value- 1] in 'XO'):
                print('Эта яйчейка уже используется, выберете другую!')
                continue
            self.board_data[value - 1] = self.player_token
            break


class WinCheking(GameBoard):
    WIN_COORD: tuple = [(1, 2, 3), (4, 5, 6), (7, 8, 9), # horizontal
                        (1, 4, 7), (2, 5, 8), (3, 6, 9), # vertical
                        (1, 5, 9), (3, 5, 7)] # diag

    def check_win(self):
        for all in self.WIN_COORD:
            if (self.board_data[all[0] - 1] == self.board_data[all[1] - 1] 
                == self.board_data[all[2] - 1]):
                return self.board_data[all[1] - 1]
            else:
                return False


def main(gameboard: GameBoard,
         game: Game,
         win: WinCheking):
    counter = 0
    while True:
        gaming = gameboard.draw_board()
        print(gaming(VALUES))
        if counter % 2 == 0:
            x = game.input_values('X')
            
        else:
            o = game.input_values('O')
        if counter > 3:
            winner = win.check_win()
            if winner:
                gaming
                print(winner, 'Выиграл')
                break
        counter += 1

        if counter > COUNTER1:
            print('Ничья!')
            break



    


