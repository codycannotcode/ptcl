import pygame

class Game():
  screen = None

  def __init__(self, width, height, rows=200, cols=200):
    pygame.init()
    self.width = width
    self.height = height
    self.screen = pygame.display.set_mode((width, height))
    self.clock = pygame.time.Clock()
    self.running = True
    self.grid = [[None]*cols]*rows
    
  def run(self):
    while self.running:
      
      self.render()
      pygame.display.flip()
      self.clock.tick(60)

  def render(self):
    pygame.draw.rect(
      self.screen,
      (255,255,255),
      pygame.Rect((100, 100), (5, 5))
    )
    
    for r in range(len(self.grid)):
      for c in range(len(self.grid[r])):
        pass

  def handle_events(self):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.running = False