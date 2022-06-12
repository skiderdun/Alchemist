import pygame
from settings import *
from tile import Tile
from player import Player
from debug import debug

class Level:
	def __init__(self):
		# display surface
		self.display_surface = pygame.display.get_surface()

		# setup sprites
		self.visible_sprites = YsortCamraGroup()
		self.obstical_sprites = pygame.sprite.Group()

		self.creat_map()

	def creat_map(self):

		for row_index, row in enumerate(alchemist_shop):
			for col_index,col in enumerate(row):
				x = col_index * Tile_size
				y = row_index * Tile_size
				if col == 'X':
					Tile((x,y),[self.visible_sprites,self.obstical_sprites])
				if col == 'P':
					self.player = Player((x,y),[self.visible_sprites],self.obstical_sprites)

	def run(self):
		# update and draw the game
		self.visible_sprites.custom_draw(self.player)
		self.visible_sprites.update()



class YsortCamraGroup(pygame.sprite.Group):
	def __init__(self):

		#genral setup
		super().__init__()
		self.display_surface = pygame.display.get_surface()
		self.half_width = self.display_surface.get_size()[0] // 2
		self.half_height = self.display_surface.get_size()[1] // 2
		self.offset = pygame.math.Vector2()

	def custom_draw(self,player):

		# get offset
		self.offset.x = player.rect.centerx - self.half_width
		self.offset.y = player.rect.centery - self.half_height

		for sprite in self.sprites():
			offset_pos = sprite.rect.topleft - self.offset
			self.display_surface.blit(sprite.image,offset_pos)