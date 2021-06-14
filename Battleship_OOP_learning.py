import random
ships = {'carrier': 5, 'battleship': 4, 'cruiser': 3, 'submarine': 3, 'destroyer': 2}
moves = 10
grid_length = 10
all_coords = set()
list_of_ships = []
list_of_ship_names = []

player_board = [] # reset board - clears everything
            
for x in range(grid_length):
    player_board.append(["0"] * grid_length)

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

    def occupied_squares(self):
        a = []
        for i in range(self.length):

            # this creates list of tuples

            if self.orientation == True:
                    a.append((self.y_coord, self.x_coord + i))

                    # creates tuple of coords

            else:
                a.append((self.y_coord + i, self.x_coord))

        return a
                    

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
            board = player_board

            list_of_ships = []
            list_of_ship_names = []
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

                list_of_ship_names.append(BattleShip.name)

                
                char1 = list_of_ships[index].name
                # first letter of name of ship type

                all_coords.update(list_of_ships[index].occupied_squares())
                # apparently set can't absorb nested list - have to convert nested list into flat list first



                # I think this can be shortened using the occupied squares def at the top
                if orientation == True:
                    board[y_coord][x_coord:x_coord + length] = char1 * length

                else:
                    for i in range(length):
                        board[y_coord + i][x_coord] = char1

        except IndexError:
            continue
        # redoes the entire thing again if outta index; if nothing fails, breaks outta loop

        if len(all_coords)!=sum(ships.values()):
            continue
        # redoes entire thing if total number of squares ships occupy != total len of ships (overlap)

        return board

board = set_ships()

# write regex expression to check input validation

while True:
    player_input = input()
    x = int(player_input[0])
    y = int(player_input[1])

    if board[y][x] == '0':
        player_board[y][x] = 'N'
    else:
        ship_hit = board[y][x] # this is a string value
        index = list_of_ship_names.index(ship_hit)
        list_of_ships[index].hp -= 1
        player_board[y][x] = 'X'
        pass



    board[y][x] = 'X'




print_board(board)

print(all_coords)