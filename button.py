from turtle import width
from pygame import Surface, Rect
from pygame.font import Font

class Button():
  font: Font
  width: int
  height: int

  def __init__(self, particle, width, height):
    self.text = particle.__name__
    self.color = particle.color
    self.surface = Surface((width, height))
    self.surface.fill(self.color)
    self.text = self.font.render(self.text, True, (0, 0, 0))
    self.surface.blit(self.text, (
      width / 2 - self.text.get_width() / 2,
      height / 2 - self.text.get_height() / 2
      ))