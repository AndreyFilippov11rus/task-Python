class Cell:
    def __init__(self, number, status='free'):
        self.status = status
        self.number = number


class Board:
    def __init__(self):
        self.list_board = [Cell(numb) for numb in range(1, 11)]

    def print_board(self):
        print('-------------')
        for i in range(3):
            print('|', self.list_board[0 + i * 3].number, '|', self.list_board[1 + i * 3].number, '|', self.list_board[2 + i * 3].number, '|')
            print('-------------')


    def change_board(self, mark, symbol):
        if self.list_board[mark - 1].status == 'free':
            self.list_board[mark - 1].status = 'close'
            self.list_board[mark - 1].number = symbol
        else:
            return False


class Player:
    def __init__(self, name):
        self.name = name
        self.list_step = []


def step(player, symbol):
    print(f'Текущее поле: ')
    board.print_board()
    mark = int(input(f'{player.name}, введите номер клетки, на которую хотите поставить {symbol}: '))
    status = board.change_board(mark, symbol)
    if status == False:
        print('Клетка занята. Повторите попытку.')
        step(player, symbol)
    player.list_step.append(mark)
    for win in win_list:
        if len(set(win) & set(player.list_step)) == 3:
            print(f'{player.name} победил!')
            board.print_board()
            return True
    if len(player1.list_step) + len(player2.list_step) == 9:
        print('Ничья!')
        return True


win_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
board = Board()
player1 = Player('Иван Иваныч')
player2 = Player('Джон Траволтыч')

while True:
    flag = step(player1, "X")
    if flag == True:
        break
    flag = step(player2, "O")
    if flag == True:
        break
