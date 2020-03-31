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

    def is_possible(self):
        if len(self.neighbours) is not len(self.connected):
            return True
        else:
            return False

    def neighbours_to(self):
        neighbours = []
        for dot in self.neighbours:
            if not dot.played:
                neighbours.append(dot)

        return f'{self.x}{self.y} is a neighbour to: {neighbours}'

    def __repr__(self):
        return f'{self.x}{self.y}'

    def __str__(self):
        return f'{self.look}'


def create_grid(m, n):
    matrix = []
    for i in range(m):
        temp = []
        for j in range(n):
            temp.append(Dot((i, j)))
        matrix.append(temp)

    for i in range(m):
        for j in range(n):
            if 0 < i < m - 1 and 0 < j < n - 1:
                matrix[i][j].neighbours = [matrix[i - 1][j], matrix[i][j + 1], matrix[i + 1][j], matrix[i][j - 1]]
            elif i == 0:
                if j == 0:
                    matrix[i][j].neighbours = [matrix[i][j + 1], matrix[i + 1][j]]
                elif 0 < j < n - 1:
                    matrix[i][j].neighbours = [matrix[i][j - 1], matrix[i + 1][j], matrix[i][j + 1]]
                else:
                    matrix[i][j].neighbours = [matrix[i][j - 1], matrix[i + 1][j]]
            elif i == m - 1:
                if j == 0:
                    matrix[i][j].neighbours = [matrix[i - 1][j], matrix[i][j + 1]]
                elif 0 < j < n - 1:
                    matrix[i][j].neighbours = [matrix[i][j - 1], matrix[i - 1][j], matrix[i][j + 1]]
                else:
                    matrix[i][j].neighbours = [matrix[i][j - 1], matrix[i - 1][j]]
    return matrix


def print_grid(matrix):
    for row in matrix:
        for dot in row:
            print(dot, end='')
        print()


def play(grid, m, n):
    while True:
        try:
            x = int(input('Enter the x coordinate of the starting dot: '))
            y = int(input('Enter the y coordinate of the starting dot: '))
            if -1 < x < m and -1 < y < n and not grid[x][y].played:
                break
            else:
                print('Out of range!')
        except ValueError:
            print('Try again!')

    print(grid[x][y].neighbours_to())
    print(f'Already connected to: {grid[x][y].connected}')

    print('Choose to which do to connect: ')
    while True:
        try:
            k = int(input('Enter the x coordinate: '))
            l = int(input('Enter the y coordinate: '))
            if -1 < k < m and -1 < l < n and grid[x][y]:
                grid[x][y].look = '-'
                grid[x][y].connected.append(grid[k][l])
                grid[k][l].look = '-'
                grid[k][l].connected.append(grid[x][y])

                if grid[x][y].is_possible():
                    pass
                else:
                    grid[x][y].played = True

                if grid[k][l].is_possible():
                    pass
                else:
                    grid[k][l].played = True
                break
            else:
                print('Out of range!')
        except ValueError:
            print('Try again!')


def main():
    while True:
        try:
            m = int(input('Enter number of dots (row): '))
            n = int(input('Enter number of dots (column): '))
            break
        except ValueError:
            print('Try again.')
            pass

    grid = create_grid(m, n)
    while True:
        print_grid(grid)
        play(grid, m, n)


if __name__ == '__main__':
    main()
