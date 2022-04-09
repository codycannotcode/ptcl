from pygame import Surface, Rect
from pygame.font import Font

class Button():
  font: Font

  def __init__(self, particle_cls):
    self.surface = self.font.render('hi', True, (255, 255 ,255))