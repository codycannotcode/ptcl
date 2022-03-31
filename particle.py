from dataclasses import dataclass

@dataclass
class Particle():
  direction: int
  strength: int = 0
  color: tuple = (255,255,255)

  def update():
    pass

@dataclass
class BasicSand(Particle):
  strength: int = 1
  color: tuple = (255, 0, 255)

  def update(grid):
    pass