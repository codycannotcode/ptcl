from dataclasses import dataclass, field
from grid import Grid

@dataclass
class Particle():
  direction: int
  grid: Grid
  x: int = field(default=0)
  y: int = field(default=0)
  strength: int = 0
  color: tuple = (255,255,255)

  def update():
    pass

  def moveTo(self, x, y):
    #if self.grid
    pass

@dataclass
class BasicSand(Particle):
  strength: int = 1
  color: tuple = (255, 0, 255)

  def update(grid):
    pass