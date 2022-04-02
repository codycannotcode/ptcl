import pygame
import particle
import random
from grid import Grid

class Game():
  screen = None

  def __init__(self, width, height, rows=50, cols=50):
    pygame.init()
    self.WIDTH = width
    self.HEIGHT = height
    self.screen = pygame.display.set_mode((width, height))
    self.clock = pygame.time.Clock()
    self.running = True
    
    self.ROWS = rows
    self.COLS = cols
    self.grid = Grid(rows, cols)
    self.SIZE = 5

    self.grid[0][0] = particle.Particle(0)
    self.grid[25][25] = particle.Particle(0)
    
  def run(self):
    while self.running:
      
      self.action()
      self.handle_events()
      self.render()
      pygame.display.flip()
      self.clock.tick(60)


  def action(self):
    particle = random.choice(random.choice(self.grid))
    if particle:
      print(particle)

  def render(self):
    
    for r in range(len(self.grid)):
      for c in range(len(self.grid[r])):
        particle = self.grid[r][c]
        if particle:
          pygame.draw.rect(
            self.screen,
            particle.color,
            pygame.Rect(r*self.SIZE, c*self.SIZE,self.SIZE,self.SIZE),
          )

  def handle_events(self):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.running = False