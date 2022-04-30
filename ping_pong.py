import pygame
pygame.init()


width = 600
height = 500

class GameSprite(pygame.sprite.Sprite):
  def __init__(self, player_image, player_x, player_y, player_speed, width, height):
    super().__init__()
    self.image = pygame.transform.scale(pygame.image.load(player_image))
    self.speed = player_speed
    self.rect = self.image.get_rect()
    self.rect.x = player_x
    self.rect.y = player_y
    
def reset(self):
    pygame.window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_right(self):
        keys = pygame.key.get_pressed()
        if pygame.keys[pygame.K_UP] and pygame.self.rect.y > 5:
          pygame.self.rect.y -= pygame.self.speed
        if pygame.keys[pygame.K_DOWN] and pygame.self.rect.y > 420:
          pygame.self.rect.y += pygame.self.speed


    def update_left(self):
      if pygame.keys[pygame.K_w] and self.rect.y > 5:
        self.rect.y -= self.speed

      if pygame.keys[pygame.K_s] and self.rect.y > 420:
        self.rect.y += self.speed

run = True
finish = False

window = pygame.display.set_mode((width, height))

while run:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

    pygame.display.update()

