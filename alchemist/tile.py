import pygame 
from settings import *

class Tile(pygame.sprite.Sprite):
	"class for all tile types"
	def __init__(self, pos, groups):
		super().__init__(groups)
		self.image = pygame.image.load('Tiles/WALLS_1.png').convert_alpha()
		self.rect = self.image.get_rect(topleft = pos)
		self.hitbox = self.rect.inflate(0,-20)
