import pygame
pygame init ()


width = 600
height = 500

class GameSprite(sprite.Sprite):
  def __init__(self, player_image, player_x, player_y, player_speed, width, height):
    super().__init__()
    self.image = transform.scale(image.load(player_image))
    self.speed = player_speed
    self.rect = self.image.get_rect()
    self.rect.x = player_x
    self.rect.y = player_y
    
 def reset(self):
  window.blit(self.image, (self.rect.x, self.rect.y)

class Player(GameSprite):
  def update_right(self):
    keys = key.get_pressed()
    if keys[K_UP] and self.rect.y > 5:
      self.rect.y -= self.speed
    if keys[K_DOWN] and self.rect.y > 420:
      self.rect.y += self.speed


  def update_left(self):
    if keys[K_w] and self.rect.y > 5:
      self.rect.y -= self.speed

    if keys[K_s] and self.rect.y > 420:
      self.rect.y += self.speed

   
          
              
window = pygame.display.set_mode((win_width, win_height))
run = True

While run:
  run = True
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
              run = False
  pygame.display.update()
  
