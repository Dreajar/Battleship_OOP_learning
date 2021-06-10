import random

ships = {'carrier': 5, 'battleship': 4, 'cruiser': 3, 'submarine': 3, 'destroyer': 2}
moves = 10
board = []
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

    def provide_name(self):
        return self.name

    def hp_remaining(self):
        return self.hp

# ==== create board ==== #

for x in range(grid_length):
    board.append(["0"] * grid_length)

# ==== print board ==== # !!!

def print_board(board):
    for index, row in enumerate(board):

        print("|".join(row))
        
        if index != len(board)-1:
            print('-' * (len(board) * 2 - 1))
        else:
            None

# ==== set board ==== #

def set_ships(board):

    while True:
    # generate random positions
    # Note: can generate ship that will extend out of bounds
    # Solution 1: catch error, try generating all ships again
    # Solution 2: catch error, generate individual ship again

    # might need a while loop here !!!

        try:

            list_of_ships = []

            ship_x = random.sample(range(10), 5) # generate x-value
            ship_y = random.sample(range(10), 5) # generate y-value
            

            for index, (name, length) in enumerate(ships.items()):

                # generate random boolean for orientation
                # True = to the right; False = downwards
                orientation = random.choice([True, False])

                list_of_ships.append(BattleShip(name, length, orientation))

                x_coord = ship_x[index]
                y_coord = ship_y[index]

                list_of_ships[index].set_xy_coordinates(x_coord, y_coord)
                
                char = [list_of_ships[index].name][0]
                # first letter of name of ship type

                if orientation == True:
                    board[y_coord][x_coord:x_coord + length] = char * length

                else:
                    for i in range(length):
                        board[y_coord + i][x_coord] = char

        except IndexError:
            continue

        # redoes the entire thing again if outta index; if nothing fails, breaks outta loop

        break

set_ships(board)
print_board(board)