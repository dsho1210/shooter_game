# Import the module
import pygame as pg
pg.font.init()
# Create the window
WIDTH = 1040
HEIGHT = 720
window = pg.display.set_mode((WIDTH, HEIGHT))
# Create a clock object
clock = pg.time.Clock()
 
class ImageSprite(pg.sprite.Sprite):
    def __init__(self, filename, position, size, speed=(0,0)): # create the constructor (runs when a new object is created)
        self.image = pg.image.load(filename)
        self.image = pg.transform.scale(self.image, size)
        self.rect = pg.Rect(position, size)
        self.speed = pg.Vector2(speed)
    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)

class Player(ImageSprite):
    def __init__(self, filename, position, size, speed=(0,0)):
        super().__init__(filename, position, size, speed)
        self.original_pos = position
    def reset(self):
        self.rect.topleft = self.original_pos
    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.rect.x -= self.speed.x
        if keys[pg.K_d]:
            self.rect.x += self.speed.x
 
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
background =  ImageSprite(filename='galaxy.jpg', position=(0,0),  size = (WIDTH, HEIGHT))

# Create the MAIN loop
while not pg.event.peek(pg.QUIT):
    window.fill((255,255,255))
    player.update()
    enemy.update()
    for w in walls:
        if player.is_colliding_with(w):
            player.reset()
            lives-=1
            point_counter.set_text('Lives:' + str(lives))
            
    if lives<=0:
        break

    if player.is_colliding_with(enemy):
        window.fill((10, 10, 10))
        player.reset()
    if player.is_colliding_with(goal):
        window.fill((20, 20, 20))
    
 
    
    # update the screen
    pg.display.update()
    # tick the clock
    clock.tick(60)
window.fill((0, 0, 0))
game_over.set_text('Game Over')
game_over.draw(window, bg =  False)
pg.display.update()
pg.time.delay(2000)

 

