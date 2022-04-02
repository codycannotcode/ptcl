from particle import Particle

class Grid():
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.__grid = [[None]*cols for _ in range(rows)]

    def in_range(self, x, y):
        return y > 0 and y < self.rows - 1 and x > 0 and x < self.cols

    def set(self, x, y, particle: Particle):
        self.__grid[y][x] = particle
        particle.x = x
        particle.y = y
    
    def get(self, x, y):
        return self.__grid[y][x]