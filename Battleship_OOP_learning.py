import random
ships = {'carrier': 5, 'battleship': 4, 'cruiser': 3, 'submarine': 3, 'destroyer': 2}
moves = 10
grid_length = 10

# ==== creating class BattleShip ==== #

class BattleShip:
    def __init__(self, name, length, orientation):
        self.name = name
        self.length = length
        self.hp = length
        self.orientation = orientation

    def set_xy_coordinates(self, x_coord, y_coord):
        self.x_coord = x_coord
        self.y_coord = y_coord

# ==== print board ==== # !!!

def print_board(board):
    for index, row in enumerate(board):

        print("|".join(row))
        
        if index != len(board)-1:
            print('-' * (len(board) * 2 - 1))

# ==== set board ==== #

def set_ships():
    while True:
        try:
            board = [] # reset board - clears everything

            for x in range(grid_length):
                board.append(["0"] * grid_length)
            # remakes 10x10 grid

            list_of_ships = []
            # clears list of ship objects

            ship_x = random.sample(range(10), 5) # generate x-value
            ship_y = random.sample(range(10), 5) # generate y-value
            
            for index, (name, length) in enumerate(ships.items()):

                # generate random boolean for orientation
                # True = to the right; False = downwards
                orientation = random.choice([True, False])
                x_coord = ship_x[index]
                y_coord = ship_y[index]

                list_of_ships.append(BattleShip(name, length, orientation))
                list_of_ships[index].set_xy_coordinates(x_coord, y_coord)
                
                char1 = list_of_ships[index].name[0]
                # first letter of name of ship type

                if orientation == True:
                    board[y_coord][x_coord:x_coord + length] = char1 * length

                else:
                    for i in range(length):
                        board[y_coord + i][x_coord] = char1

        except IndexError:
            continue

        # redoes the entire thing again if outta index; if nothing fails, breaks outta loop

        return board

        break

board = set_ships()
print_board(board)