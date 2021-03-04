N_ROWS= 6
N_COLS= 7
def init():
  board = [["."]*N_ROWS]*N_COLS
  return board
init()
def print_board(board):
  text = ''
  
  for i in range (N_COLS):
    text += str(i+1) + " "
  print(text)
  print("-" * (2 * N_COLS -1))
  for row in board:
    print("|".join(row))
def get_move(board, player):
  col = input("Player {} enter a column".format(player))
  if not is_valid_col(col):
    print("wrong! Input a value between 1 and {}".format(N_COLS))
    col = get_move(board, player)
  col = col-1
  placed = False
  for i in range(len(board)-1,-1,-1):
    if not placed and (board[r][col] == "."):
      board[r][col] = player
      placed = True
def is_valid_col(col):
  return col>0 and col <= N_COLS

def make_move():
  placed = False
  r = len(board) -1
  while not placed and r>=0:
    if board[r][col]:
def has_won():
  return row_won(board, player) or col_won(board, player) of left_diag_won(board,player) or right_diag_won(board,player)
def row_won(board, player):
  has_won = False
  r=0
  while r<N_ROWS and not has_won:
    c=0
    num_consecutive = 0
    while c < N_COLS and not has_won():
      if board[r][c] == player:
        num_consecutive += 1
        print("detected {} at r = {}, c = {},n_c = {}".format(player, r, c, num_consecutive))
      else:
        num_consecutive = 0
      has_won = num_consecutive>=4
      c += 1
    r+= 1
  return has_won
def col_won():
  return False




def main():
  board = init()
  print_board(board)
  get_move(board , "x")
main()