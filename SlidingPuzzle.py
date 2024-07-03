# This program allows the user to play a sliding puzzle game from tiles given
# as a sequence of numbers separated by commas, by calling e.g. main("2,3,1,").
# The aim is to get all the tiles in order from left to right. Puzzle sequences
# have not been provided.
# Written for COMPSCI 101.

def main(tiles):
    list_of_tiles = tiles.split(',')
    grid_size = get_size(list_of_tiles)
    draw_grid(grid_size, list_of_tiles)
    continue_game(grid_size, list_of_tiles)

def continue_game(grid_size, list_of_tiles):
    ongoing_game, moves_counter = True, 0
    while ongoing_game:
        if is_complete(list_of_tiles):
            print("You won in", moves_counter, "moves. Congratulations!")
            ongoing_game = False
        else:
            tile_choice = get_input(grid_size, list_of_tiles)
            if tile_choice == "quit":
                ongoing_game = False
            else:
                swap_tile(list_of_tiles, tile_choice)
                draw_grid(grid_size, list_of_tiles)
        moves_counter += 1

def get_size(list_of_values):
    from math import sqrt
    grid_length = round(sqrt(len(list_of_values)))
    return grid_length

def draw_row(list_of_values):
    row = ['│']
    for value in list_of_values:
        if len(value) == 0:
            row.append('    │')
        elif len(value) == 1:
            row.append('  ' + value + ' │')
        elif len(value) == 2:
            row.append(' ' + value + ' │')
    print(''.join(row))

def draw_grid_line(opening_edge, closing_edge, connector, grid_size):
    row = []
    for row_size in range(grid_size):
        row.append('────')
    row = opening_edge + connector.join(row) + closing_edge
    print(row)

def draw_grid(grid_size, list_of_tiles):
    draw_grid_line('┌', '┐', '┬', grid_size)
    for row in range(grid_size):
        draw_row(list_of_tiles[(row * grid_size):((row + 1) * grid_size)])
        if row != grid_size - 1:
            draw_grid_line('├', '┤', '┼', grid_size)
    draw_grid_line('└', '┘', '┴', grid_size)

def get_input(grid_size, list_of_tiles):
    prompt = "Your move: "
    choice = input(prompt)
    while not validate_choice(choice, grid_size, list_of_tiles):
        print(choice, "is not valid. Try again.")
        choice = input(prompt)
    return choice

def validate_choice(choice, grid_size, list_of_tiles):
    blank_index, tile_index = 0, 0
    if choice in list_of_tiles:
        blank_index = list_of_tiles.index('')
        tile_index = list_of_tiles.index(choice)
    is_valid = (
                choice == "quit" or
                is_vertically_adjacent(grid_size, tile_index, blank_index) or
                is_horizontally_adjacent(grid_size, tile_index, blank_index)
                )
    return is_valid

def is_vertically_adjacent(grid_size, tile_index, blank_index):
    vertically_adjacent = (
                            blank_index - tile_index == grid_size or
                            tile_index - blank_index == grid_size
                            )
    return vertically_adjacent

def is_horizontally_adjacent(grid_size, tile_index, blank_index):
    horizontally_adjacent = (
                            (blank_index - tile_index == 1 or
                            tile_index - blank_index == 1)
                            and
                            blank_index // grid_size == tile_index // grid_size
                            )
    return horizontally_adjacent

def swap_tile(list_of_tiles, tile_choice):
    tile_index = list_of_tiles.index(tile_choice)
    blank_index = list_of_tiles.index('')

    list_of_tiles.insert(tile_index, '')
    list_of_tiles.pop(tile_index + 1)
    list_of_tiles.insert(blank_index, tile_choice)
    list_of_tiles.pop(blank_index + 1)

def strings_to_integers_list(list_of_tiles):
    digit_tiles = []
    for tile in list_of_tiles:
        if tile.isdigit():
            digit_tiles.append(int(tile))
        else:
            digit_tiles.append(tile)
    return digit_tiles

def is_complete(list_of_tiles):
    space_at_end = list_of_tiles[-1] == ''
    list_of_tiles = strings_to_integers_list(list_of_tiles)
    list_of_tiles.pop(list_of_tiles.index(''))
    return space_at_end and list_of_tiles == sorted(list_of_tiles)
