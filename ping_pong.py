import pygame
pygame.init()


width = 600
height = 500

back = (200, 255, 255)

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

clock = time.Clock 
FPS = 60

l_racket = Player("PingPong_racket.png", 30, 200, 4, 50, 150)
r_racket = Player("PingPong_racket.png", 520, 200, 4, 50, 150)
ball = GameSprite("PingPong_ball.png", 520, 200, 4, 50, 150

window = pygame.display.set_mode((width, height))
#window.fill(back)
                  
font.init()
font = font.Font(None, 35)
lose_l = font.render("Player left lost!", True, (180, 0, 0))
lose_r = font.render("Player right lost!", True, (0, 255, 0))

speed_x = 3
speed_y = 3

while run:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
  if finish != True:
    window.fill(back)                 
    l_racket.update_l()
    r_racket.update_r()
    ball.rect.x += speed_x
    ball.rect.y += speed_y
    if sprite.collide_rect(l_racket, ball) or (r_racket, ball):
        speed_x *= -1
        speed_y *= -1
    if ball.rect.y > win_height - 50 or ball.rect.y < 0:
         speed_y *= -1
    if ball.rect.x < 5:
        finish = True
        window.blit(lose_l, (200, 200))
    if ball.rect.x > win_width:
        finish = True
        window.blit(lose_r, (200, 200))
  
   l_racket.reset()
   r_racket.reset()
   ball.reset()

    pygame.display.update()
    clock.tick(FPS)

