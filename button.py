from turtle import width
from pygame import Surface, Rect, draw
from pygame.font import Font

class Button():
  font: Font
  grey_color = (122, 122, 122)

  def __init__(self, particle, x, y, width, height):
    self.particle = particle
    self.text = particle.__name__
    self.color = particle.color
    self.rect = Rect(x, y, width, height)
    self.surface = Surface((width, height))
    self.text = self.font.render(self.text, True, (0, 0, 0))
    self.render_grey()

  def render_color(self):
    self.surface.fill(self.color)
    self.surface.blit(self.text, (
      self.rect.width / 2 - self.text.get_width() / 2,
      self.rect.height / 2 - self.text.get_height() / 2
      ))
  
  def render_grey(self):
    self.surface.fill(self.grey_color)
    self.surface.blit(self.text, (
      self.rect.width / 2 - self.text.get_width() / 2,
      self.rect.height / 2 - self.text.get_height() / 2
      ))
  
  def box(self):
    draw.rect(
      self.surface,
      (0, 0, 0),
      self.rect,
      width=3
      )