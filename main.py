import numpy as np

grid = []
m = 0
n = 0
human = True
player_one_pts = 0
player_two_pts = 0


def create_grid():
    global m
    global n
    if m == 1 or m == 0:
        m = 2
    if n == 1 or n == 0:
        n = 2
    if m % 2 == 1:
        m += 1
    if n % 2 == 1:
        n += 1
    matrix = []
    for i in range(m):
        temp = []
        for j in range(n):
            temp.append(' ')
        matrix.append(temp)

    return matrix


def print_matrix(matrix):
    print('CURRENT MATRIX')
    for row in matrix:
        print(row)


def play():
    global human
    global m
    global n
    global player_one_pts
    global player_two_pts

    if human:
        print('Player one plays!')
    else:
        print('Player two plays!')

    # Checks validity
    while True:
        x = int(input('Enter x coordinate: '))
        if 0 <= x < m:
            y = int(input('Enter y coordinate: '))
            if 0 <= y < n:
                if grid[x][y] is ' ':
                    grid[x][y] = '-'
                    try:
                        # This could have been implemented way better but i'm too lazy
                        if grid[x - 1][y] is '-' and grid[x - 1][y - 1] is '-' and grid[x][y - 1] is '-':
                            try:
                                grid[x - 1][y] = '#'
                                grid[x - 1][y - 1] = '#'
                                grid[x][y - 1] = '#'
                                grid[x][y] = '#'
                                if human:
                                    player_one_pts += 10
                                else:
                                    player_two_pts += 10
                            except IndexError:
                                pass
                        elif grid[x - 1][y] is '-' and grid[x - 1][y + 1] is '-' and grid[x][y + 1] is '-':
                            try:
                                grid[x - 1][y] = '#'
                                grid[x - 1][y + 1] = '#'
                                grid[x][y + 1] = '#'
                                grid[x][y] = '#'
                                if human:
                                    player_one_pts += 10
                                else:
                                    player_two_pts += 10
                            except IndexError:
                                pass
                        elif grid[x][y + 1] is '-' and grid[x + 1][y + 1] is '-' and grid[x + 1][y] is '-':
                            try:
                                grid[x][y + 1] = '#'
                                grid[x + 1][y + 1] = '#'
                                grid[x + 1][y] = '#'
                                grid[x][y] = '#'
                                if human:
                                    player_one_pts += 10
                                else:
                                    player_two_pts += 10
                            except IndexError:
                                pass
                        elif grid[x + 1][y] is '-' and grid[x + 1][y - 1] is '-' and grid[x][y - 1] is '-':
                            try:
                                grid[x + 1][y] = '#'
                                grid[x + 1][y - 1] = '#'
                                grid[x][y - 1] = '#'
                                grid[x][y] = '#'
                                if human:
                                    player_one_pts += 10
                                else:
                                    player_two_pts += 10
                            except IndexError:
                                pass
                        else:
                            human = not human
                    except IndexError:
                        pass
                    break
                else:
                    print('Bad input. Try again!')
                    print_matrix(grid)
        else:
            continue


def check_end():
    for i in range(m):
        for j in range(n):
            if grid[i][j] is ' ':
                return False
    if player_one_pts > player_two_pts:
        print('Player one wins!')
    elif player_one_pts == player_two_pts:
        print('Even!')
    else:
        print('Player two wins!')
    return True


def main():
    global grid
    global m
    global n

    while True:
        try:
            m = int(input('Enter number of rows: '))
            n = int(input('Enter number of columns: '))
        except ValueError:
            print('Bad input. Try again!')
        else:
            break

    grid = create_grid()

    while True:
        print_matrix(grid)
        play()
        if check_end():
            print('END!')
            break


if __name__ == '__main__':
    main()
