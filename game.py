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
    self.mouse_down = False

    self.grid = Grid(int(height/self.SIZE), int(width/self.SIZE))
    particle.Particle.grid = self.grid
    
  def run(self):
    while self.running:

      self.handle_events()
      self.step()
      self.render()
      pygame.display.flip()
      self.clock.tick(60)
  
  def step(self):
    step_queue = []
    
    for x in range(self.grid.cols):
      for y in range(self.grid.rows):
        particle = self.grid.get(x, y)
        if particle:
          step_queue.append(particle)

    for i, particle in enumerate(step_queue):
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
        elif event.type == pygame.MOUSEMOTION:
          if self.mouse_down:
            self.onDrag()
        elif event.type == pygame.MOUSEBUTTONDOWN:
          self.mouse_down = True
        elif event.type == pygame.MOUSEBUTTONUP:
          self.mouse_down = False
  
  def onDrag(self):
    mousePos = pygame.mouse.get_pos()
    x, y = int(mousePos[0] / self.SIZE), int(mousePos[1] / self.SIZE)
    if not self.grid.get(x, y):
      particle.Sand(x, y)