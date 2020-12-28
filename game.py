import pygame

class Bat(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super().__init__()
		
		spriteSize = 48

		self.image = pygame.transform.scale(pygame.image.load("sprite2.png"), (spriteSize,spriteSize))
		self.rect = self.image.get_rect()		

		self.flap2 = pygame.transform.scale(pygame.image.load("sprite2.png"), (spriteSize,spriteSize))
		self.flap3 = pygame.transform.scale(pygame.image.load("sprite3.png"), (spriteSize, spriteSize))
		self.dead = pygame.transform.scale(pygame.image.load("deadSprite.png"), (spriteSize, spriteSize))

		self.rect.x = x
		self.rect.y = y

		self.changeX = 0
		self.changeY = 0

	def changeSpeed(self,isMoving,isDead):
		if isDead == False:
			if isMoving == True:
				self.changeY -= 1
			if isMoving == False:
				self.changeY +=.9
		elif isDead == True:
			self.changeY = 0
		self.rect.y += self.changeY
pygame.init()
displayWidth = 288
displayHeight = 512
screen = pygame.display.set_mode((displayWidth,displayHeight))
clock = pygame.time.Clock()

bat1 = Bat(100,100)
batGroup = pygame.sprite.Group()
batGroup.add(bat1)

isDead = False
pressed = False
gameExit = True
while gameExit == True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameExit=False
		#movement
        if (bat1.rect.y < displayHeight-19):
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed = True
                    bat1.image = bat1.flap3
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    pressed = False
                    bat1.image = bat1.flap2
    screen.fill((0,0,0))
    batGroup.draw(screen)
    bat1.changeSpeed(pressed,isDead)
    pygame.display.update()
    clock.tick(30)

pygame.quit()
quit()
