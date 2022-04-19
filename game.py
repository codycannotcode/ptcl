from sys import flags
import pygame
import particles.particle as particle
from grid import Grid
from button import Button
import numpy as np

class Game():
  screen = None

  def __init__(self, width, height):
    pygame.init()

    #visual constants
    self.WIDTH = width
    self.HEIGHT = height
    self.BAR_WIDTH = 70
    self.PIXEL_SIZE = 5
    self.BUTTON_HEIGHT = 30
    self.BUTTON_WIDTH = 50
    self.BG_COLOR = (0, 0, 0)
    self.BAR_COLOR = (31, 31, 31)

    self.screen = pygame.display.set_mode((width, height))
    self.clock = pygame.time.Clock()
    self.font = pygame.font.Font(None, 25)
    Button.font = self.font

    self.running = True
    self.mouse_down = False
    self.selected_particle = None
    self.hovered_button = None
    self.selected_button = None
    
    self.bar = pygame.Surface((self.BAR_WIDTH, self.HEIGHT))
    self.bar.fill(self.BAR_COLOR)
    self.buttons: list[Button] = self.create_buttons([
      particle.Sand
    ])

    self.grid = Grid(int(height/self.PIXEL_SIZE), int((width - self.BAR_WIDTH)/self.PIXEL_SIZE))
    particle.Particle.grid = self.grid
    
  def create_buttons(self, particle_types):
    buttons = []
    for i, particle in enumerate(particle_types):
      buttons.append(
        Button(
          particle,
          self.WIDTH - self.BAR_WIDTH + 10,
          self.HEIGHT / 2 - i * (self.BUTTON_HEIGHT+10),
          self.BUTTON_WIDTH,
          self.BUTTON_HEIGHT
        )
      )
    return buttons

  def run(self):
    while self.running:

      self.handle_events()
      self.handle_mouse()
      self.step()
      self.render()
      pygame.display.flip()
      self.clock.tick(60)
  
  def step(self):
    step_queue = []

    # for x in range(self.grid.cols-1, -1, -1):
    #   for y in range(self.grid.rows-1, -1, -1):
    #     particle = self.grid.get(x, y)
    #     if particle:
    #       step_queue.append(particle)
    particles = np.reshape(self.grid.grid(), self.grid.rows * self.grid.cols)
    
    for p in particles.flat[::-1]:
      if p:
        step_queue.append(p)

    for particle in np.array(step_queue).flat:
      particle.step()

  def render(self):
    self.screen.fill(self.BG_COLOR)
    self.screen.blit(self.bar, (self.WIDTH - self.BAR_WIDTH, 0))

    for button in self.buttons:
      self.screen.blit(button.surface, button.rect)

    particles = np.reshape(self.grid.grid(), self.grid.rows * self.grid.cols)
    
    for p in particles.flat:
      if p:
        pygame.draw.rect(
          self.screen,
          p.color,
          pygame.Rect(p.x*self.PIXEL_SIZE, p.y*self.PIXEL_SIZE,self.PIXEL_SIZE,self.PIXEL_SIZE),
        )

  def handle_events(self):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
          self.mouse_clicked()
        elif event.type == pygame.MOUSEBUTTONUP:
          self.mouse_down = False

  def mouse_clicked(self):
    self.mouse_down = True
    if self.hovered_button:
      print('yeah')
      if self.hovered_button != self.selected_button:
        self.selected_button = self.hovered_button
        self.selected_button.selected()
        self.hovered_button = None
      else:
        print('yeah')
  
  def handle_mouse(self):
    mousePos = pygame.mouse.get_pos()
    found_button = False
    for button in self.buttons:
      if button.rect.collidepoint(mousePos):
        self.hovered_button = button
        button.hovered()
        found_button = True
        break

    if not found_button:
      if self.hovered_button:
        self.hovered_button.unhovered()
      self.hovered_button = None

    if self.mouse_down:
      self.spawn_at_mouse()
  
  def spawn_at_mouse(self):
    mousePos = pygame.mouse.get_pos()
    x, y = int(mousePos[0] / self.PIXEL_SIZE), int(mousePos[1] / self.PIXEL_SIZE)
    if self.grid.in_range(x, y):
      particle.Sand(x, y)