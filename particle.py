from grid import Grid

class Particle():
  grid: Grid
  color: tuple = (255,255,255)

  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.stepped = False
    self.grid.set(x, y, self)

  def step(self):
    if self.stepped: return
    
    if self.grid.in_range(self.x, self.y+1):
      other = self.grid.get(self.x, self.y+1)
      if not other:
        cur_y = self.y
        self.grid.set(self.x, cur_y+1, self)
        self.grid.set(self.x, cur_y, None)
    
    self.stepped = True