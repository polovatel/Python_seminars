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

# game = GameBoard(list(range(1,10)))
# game.draw_board()
    

class Game:
    pass