class TikTok:
    #TODO: ADD start game method
    #TODO: complete "has_player_win" method
    
    def __init__(self):
        self.board = list(map(str, range(10)))
        self.player_turn = 'X'
        
        
    def show_board(self):
        print("\n")
        print(self.board[1] + '|' + self.board[2] + '|' + self.board[3])
        print('-'*5)
        
        print(self.board[4] + '|' + self.board[5] + '|' + self.board[6])
        print('-'*5)
        
        print(self.board[7] + '|' + self.board[8] + '|' + self.board[9])
        
    
    def swap_player_turn(self):
        self.player_turn = 'X' if self.player_turn == 'O' else 'O'
        return self.player_turn
        
        
    def is_board_filled(self):
        return ' ' not in self.board[1:]
    
    def fix_spot(self, cell, player):
        self.board[cell] = player
        
        
    def has_player_win(self, player):
        win_combo = [
            [1,2,3], [4,5,6], [7,8,9],
            [1,4,7], [2,5,8], [3,6,9],
            [1,5,9], [3,5,7]
        ]
        