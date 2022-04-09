import pygame
import particles.particle as particle
from grid import Grid
from button import Button

class Game():
  screen = None

  def __init__(self, width, height):
    pygame.init()

    #visual constants
    self.WIDTH = width
    self.HEIGHT = height
    self.BAR_WIDTH = 70
    self.PIXEL_SIZE = 5
    self.BUTTON_HEIGHT = 40
    self.BUTTON_WIDTH = 50
    self.BG_COLOR = (0, 0, 0)

    self.screen = pygame.display.set_mode((width, height))
    self.clock = pygame.time.Clock()
    self.font = pygame.font.Font(None, 30)
    Button.font = self.font

    self.running = True
    self.mouse_down = False

    self.buttons = [Button(particle.Sand)]

    self.grid = Grid(int(height/self.PIXEL_SIZE), int((width - self.BAR_WIDTH)/self.PIXEL_SIZE))
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
    
    for x in range(self.grid.cols-1, -1, -1):
      for y in range(self.grid.rows-1, -1, -1):
        particle = self.grid.get(x, y)
        if particle:
          step_queue.append(particle)

    for particle in step_queue:
      particle.step()

  def render(self):
    self.screen.fill(self.BG_COLOR)

    for button in self.buttons:
      self.screen.blit(button.surface, pygame.Rect(
        self.BUTTON_WIDTH, self.BUTTON_HEIGHT,
        self.WIDTH / 2, self.HEIGHT / 2
        ))
      print(button.surface)

    for r in range(self.grid.rows):
      for c in range(self.grid.cols):
        particle = self.grid.get(c, r)
        if particle:
          pygame.draw.rect(
            self.screen,
            particle.color,
            pygame.Rect(c*self.PIXEL_SIZE, r*self.PIXEL_SIZE,self.PIXEL_SIZE,self.PIXEL_SIZE),
          )

  def handle_events(self):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
          self.mouse_down = True
        elif event.type == pygame.MOUSEBUTTONUP:
          self.mouse_down = False

    if self.mouse_down:
      self.spawn_at_mouse()
  
  def spawn_at_mouse(self):
    mousePos = pygame.mouse.get_pos()
    x, y = int(mousePos[0] / self.PIXEL_SIZE), int(mousePos[1] / self.PIXEL_SIZE)
    if self.grid.in_range(x, y):
      particle.Sand(x, y)