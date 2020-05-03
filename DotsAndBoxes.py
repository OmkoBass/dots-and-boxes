turn = True
player_one_pts = 0
player_two_pts = 0
done = []


class Dot:
    def __init__(self, point=None):
        if point:
            self.x = point[0]
            self.y = point[1]
        else:
            pass
        self.played = False
        self.look = '.'
        self.neighbours = []
        self.connected = []

    # Compares two dots, return True if they are the same
    def __eq__(self, other):
        if self.x is other.x and self.y is other.y:
            return True
        else:
            return False

    def __repr__(self):
        return f'{self.x}{self.y}'

    def __str__(self):
        return f'{self.look}'

    # Return true if you can play the dot
    def is_possible(self):
        if len(self.neighbours) is not len(self.connected):
            return True
        else:
            return False

    # Display neighbours to a dot and sort them
    def neighbours_to(self):
        neighbours = []
        for dot in self.neighbours:
            if not dot.played:
                neighbours.append(dot)

        sorted(neighbours, key=lambda dots: dot.x)

        return f'{self.x}{self.y} is a neighbour to: {neighbours}'


class space:
    def __init__(self):
        self.look = ' '
        self.played = False

    def __str__(self):
        return f'{self.look}'


def create_grid(m, n):
    matrix = []

    # First we create a dot, then we create blank space for line, then dot and so on
    for i in range(m):
        temp = []
        for j in range(n):
            if i % 2 == 0 and j % 2 == 0:
                temp.append(Dot((i, j)))
            else:
                temp.append(space())
        matrix.append(temp)

    # Now since the indexing is moved these are the rules for connecting everyone,
    # [0][0] has a neighbour left to it and below it
    # [1][1] has a neighbour everywhere around him (except diagonal)
    for i in range(m):
        for j in range(n):
            if i % 2 == 0 and j % 2 == 0:
                if 0 < i < m - 1 and 0 < j < n - 1:
                    matrix[i][j].neighbours = [matrix[i - 2][j], matrix[i][j + 2], matrix[i + 2][j], matrix[i][j - 2]]
                elif i == 0:
                    if j == 0:
                        matrix[i][j].neighbours = [matrix[i][j + 2], matrix[i + 2][j]]
                    elif 0 < j < n - 1:
                        matrix[i][j].neighbours = [matrix[i][j - 2], matrix[i + 2][j], matrix[i][j + 2]]
                    else:
                        matrix[i][j].neighbours = [matrix[i][j - 2], matrix[i + 2][j]]
                elif i == m - 1:
                    if j == 0:
                        matrix[i][j].neighbours = [matrix[i - 2][j], matrix[i][j + 2]]
                    elif 0 < j < n - 1:
                        matrix[i][j].neighbours = [matrix[i][j - 2], matrix[i - 2][j], matrix[i][j + 2]]
                    else:
                        matrix[i][j].neighbours = [matrix[i][j - 2], matrix[i - 2][j]]
                elif j == 0:
                    if 0 < i < m - 1:
                        matrix[i][j].neighbours = [matrix[i - 2][j], matrix[i][j + 2], matrix[i + 2][j]]
                elif j == n - 1:
                    if 0 < i < m - 1:
                        matrix[i][j].neighbours = [matrix[i - 2][j], matrix[i][j - 2], matrix[i + 2][j]]
    return matrix


def print_grid(matrix):
    for row in matrix:
        for dot in row:
            print(dot, end='')
        print()


def play(grid, m, n):
    global turn
    global player_one_pts
    global player_two_pts

    # turn True means player, turn False means player two or AI

    if turn:
        print('Player one plays!')
    else:
        print('Player two plays!')

    while True:
        try:
            x = int(input('Enter the x coordinate of the starting dot: '))
            y = int(input('Enter the y coordinate of the starting dot: '))
            # If not line and in range and not connected all dots
            if x % 2 == 0 and y % 2 == 0:
                if -1 < x < m and -1 < y < n:
                    if not grid[x][y].played:
                        break
                    else:
                        print('Already connected everything.')
                else:
                    print('Out of range!')
            else:
                print('Only dots!')
        except ValueError:
            print('Try again!')

    print(grid[x][y].neighbours_to())
    print(f'Already connected to: {grid[x][y].connected}')

    while True:
        try:
            k = int(input('Enter the x coordinate of the destination dot: '))
            l = int(input('Enter the y coordinate of the destination dot: '))
            # Choose which to connect to
            if k % 2 == 0 and l % 2 == 0:
                if -1 < k < m and -1 < l < n and Dot((k, l)) not in grid[x][y].connected and (k is not x or l is not y):
                    if l > y:
                        grid[x][y + 1].look = '_'
                        grid[x][y + 1].played = True
                    elif k > x:
                        grid[x + 1][y].look = '|'
                        grid[x + 1][y].played = True
                    elif y > l:
                        grid[x][y - 1].look = '_'
                        grid[x][y - 1].played = True
                    elif x > k:
                        grid[x - 1][y].look = '|'
                        grid[x - 1][y].played = True
                    grid[x][y].connected.append(grid[k][l])
                    grid[k][l].connected.append(grid[x][y])

                    if grid[x][y].is_possible():
                        pass
                    else:
                        grid[x][y].played = True

                    if grid[k][l].is_possible():
                        pass
                    else:
                        grid[k][l].played = True

                    if check_grid(grid, m, n):
                        if turn:
                            player_one_pts += 1
                        else:
                            player_two_pts += 1
                    else:
                        turn = not turn
                else:
                    print('Out of range or already played!')
                break
            else:
                print('Only dots!')
        except ValueError:
            print('Try again!')


def check_grid(grid, m, n):
    global done
    for i in range(m):
        for j in range(n):
            # Check for 11 or 13 or 31 or 33 or positions like that
            if i % 2 == 1 and j % 2 == 1:
                if grid[i - 1][j].played and grid[i][j + 1].played and grid[i + 1][j].played and grid[i][j - 1].played \
                        and grid[i][j] not in done:
                    done.append(grid[i][j])
                    grid[i][j].look = '#'
                    return True
    return False


def end_game(end):
    if len(done) is end:
        return True
    else:
        return False


def main():
    # Input for boxes
    while True:
        try:
            m = int(input('Enter number of dots (row): '))
            n = int(input('Enter number of dots (column): '))
            if m < 1:
                m = 1
            if n < 1:
                n = 1
            break
        except ValueError:
            print('Try again.')
            pass

    # So the 3 x 3 will create 3 boxes
    m += 1
    n += 1

    # 3 x 3 means 3 boxes but we need to increase this so that lines can fit
    m += m - 1
    n += n - 1

    # This many boxes can be filled
    end = int(((m - 1) / 2) * ((n - 1) / 2))

    # Creates the grid, One dot one blank space for lines
    grid = create_grid(m, n)
    while True:
        print_grid(grid)
        play(grid, m, n)
        # Checks if the game ended
        if end_game(end):
            print_grid(grid)
            if player_one_pts > player_two_pts:
                print('Player one wins!')
            elif player_two_pts > player_one_pts:
                print('Player two wins!')
            else:
                print('Even!')
            print(f'Player one scored: {player_one_pts}')
            print(f'Player two scored: {player_two_pts}')
            break


if __name__ == '__main__':
    main()
