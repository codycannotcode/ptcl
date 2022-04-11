from turtle import width
from pygame import Surface, Rect
from pygame.font import Font

class Button():
  font: Font

  def __init__(self, particle, width, height):
    self.text = particle.__name__
    self.color = particle.color
    self.width = width
    self.height = height
    self.surface = Surface((width, height))
    self.normal_box()
    

  def normal_box(self):
    self.surface.fill(self.color)
    self.text = self.font.render(self.text, True, (0, 0, 0))
    self.surface.blit(self.text, (
      self.width / 2 - self.text.get_width() / 2,
      self.height / 2 - self.text.get_height() / 2
      ))