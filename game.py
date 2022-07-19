# Import the module
import pygame as pg
pg.font.init()
pg.mixer.init()
# Create the window
WIDTH = 800
HEIGHT = 640
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
rocket = Player(filename='pngwing.com.png', position=(WIDTH/2, HEIGHT-80), size=(100, 80), speed=(4, 0))
#enemy = 
# Create the MAIN loop  
while not pg.event.peek(pg.QUIT):
    rocket.update()

    background.draw(window)
    rocket.draw(window)
    


    #update the screen
    pg.display.update()

 

