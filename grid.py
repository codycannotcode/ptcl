class Grid():
  def __init__(self, rows, cols):
    self.rows = rows
    self.cols = cols
    self.__grid = [[None]*cols for _ in range(rows)]

  def grid(self):
    return self.__grid

  def in_range(self, x, y):
    return y >= 0 and y < self.rows and x >= 0 and x < self.cols

  def set(self, x, y, particle):
    self.__grid[y][x] = particle
    if particle:
        particle.x = x
        particle.y = y

  def get(self, x, y):
    return self.__grid[y][x]

  def swap(self, x1, y1, x2, y2):
    p1 = self.__grid[y1][x1]
    p2 = self.__grid[y2][x2]

    self.__grid[y1][x1] = p2
    self.__grid[y2][x2] = p1

    if p1:
      p1.x = x2
      p1.y = y2
    if p2:
      p2.x = x1
      p2.y = y1