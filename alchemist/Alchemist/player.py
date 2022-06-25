import pygame 
from settings import *

class Player(pygame.sprite.Sprite):
	"class for player"
	def __init__(self, pos, groups, obstacal_sprites):
		super().__init__(groups)
		self.image = pygame.image.load('Tiles/LIL_DUDE_BIRBVIEW.png').convert_alpha()
		self.rect = self.image.get_rect(topleft = pos)
		self.hitbox = self.rect.inflate(0,-30)

		self.direction = pygame.math.Vector2()
		self.speed = 5

		self.obstical_sprites = obstacal_sprites

	def input(self):
		key = pygame.key.get_pressed()

		if key[pygame.K_UP]:
			self.direction.y = -1
		elif key[pygame.K_DOWN]:
			self.direction.y = 1
		else:
			self.direction.y = 0

		if key[pygame.K_RIGHT]:
			self.direction.x = 1
		elif key[pygame.K_LEFT]:
			self.direction.x = -1
		else:
			self.direction.x = 0

	def move(self,speed):
		if self.direction.magnitude() != 0:
			self.direction = self.direction.normalize()

		self.hitbox.x += self.direction.x * speed
		self.collision('horizontal')
		self.hitbox.y += self.direction.y * speed
		self.collision('vertical')
		self.rect.center = self.hitbox.center
		

	def collision(self,direction):
		if direction == 'horizontal':
			for sprite in self.obstical_sprites:
				if sprite.hitbox.colliderect(self.hitbox):
					if self.direction.x > 0: #moving right
						self.hitbox.right = sprite.hitbox.left
					if self.direction.x < 0: # moving left
						self.hitbox.left = sprite.hitbox.right

		if direction == 'vertical':
			for sprite in self.obstical_sprites:
				if sprite.hitbox.colliderect(self.hitbox):
					if self.direction.y > 0: # moving down
						self.hitbox.bottom = sprite.hitbox.top
					if self.direction.y < 0: #moving up
						self.hitbox.top = sprite.hitbox.bottom

	def update(self):
		# update and draw
		self.input()
		self.move(self.speed)
