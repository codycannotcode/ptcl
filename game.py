import pygame
import particle
from grid import Grid

class Game():
  screen = None

  def __init__(self, width, height):
    pygame.init()

    #visual constants
    self.WIDTH = width
    self.HEIGHT = height
    self.SIZE = 5
    self.BG_COLOR = (0, 0, 0)

    self.screen = pygame.display.set_mode((width, height))
    self.clock = pygame.time.Clock()
    self.running = True

    self.grid = Grid(int(height/self.SIZE), int(width/self.SIZE))
    particle.Particle.grid = self.grid

    particle.Particle(5, 5)
    particle.Particle(5, 3)
    
  def run(self):
    while self.running:
      
      self.step()
      self.handle_events()
      self.render()
      pygame.display.flip()
      self.clock.tick(60)


  def step(self):
    for x in range(self.grid.cols):
      for y in range(self.grid.rows):
        particle = self.grid.get(x, y)
        if particle:
          particle.stepped = False
    
    for x in range(self.grid.cols):
      for y in range(self.grid.rows):
        particle = self.grid.get(x, y)
        if particle and not particle.stepped:
          particle.step()

  def render(self):
    self.screen.fill(self.BG_COLOR)
    for r in range(self.grid.rows):
      for c in range(self.grid.cols):
        particle = self.grid.get(c, r)
        if particle:
          pygame.draw.rect(
            self.screen,
            particle.color,
            pygame.Rect(c*self.SIZE, r*self.SIZE,self.SIZE,self.SIZE),
          )

  def handle_events(self):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.running = False