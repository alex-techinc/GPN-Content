from pygame import *
from random import *


init()

background_image = image.load("bg.png")
bird_image = image.load("bird.png")
pipe_image = image.load("pipe.png")
flipped_pipe_image = transform.flip(pipe_image, False, True)
coin_image = image.load("coin.png")

class Pipe ():

    def __init__(self, x, y, flipped):
        self.x = x
        self.y = y
        self.flipped = flipped

    def blit(self):
        if self.flipped:
            self.rect = screen.blit(flipped_pipe_image, (self.x, -self.y))
        else:
            self.rect = screen.blit(pipe_image, (self.x, self.y))

    def move(self):
        self.x = self.x - 2
        if self.x < -70:
            self.x = 800
            self.y = randint(100, 500)
            self.flipped = choice([True, False])
    
    def collides_with(self, bird):
        return bird.colliderect(self.rect)


#Created the Coin class
class Coin ():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def blit(self):
        self.rect = screen.blit(coin_image, (self.x, self.y))

    def move(self):
        self.x = self.x - 2
        if self.x < -70:
            self.x = 800
            self.y = randint(100, 500)

    def collected_by(self, bird):
        if bird.colliderect(self.rect):
            self.x = 800
            self.y = randint(100, 500)
            return True
        return False


init()

print("The game is about to start!")

screen = display.set_mode((800, 600))

background_image = image.load("bg.png")
bird_image = image.load("bird.png")


bird_x = 10
bird_y = 250

pipe1_object = Pipe(200, 250, False)
pipe2_object = Pipe(450, 100, False)
pipe3_object = Pipe(700, 400, True)

pipes = [pipe1_object, pipe2_object, pipe3_object]

#Made a coin
coin = Coin(400, 150)

#Made a points variable
points = 0

over = False

while True:

    new_event = event.poll()
    if new_event.type == KEYDOWN and new_event.key == K_UP:
        bird_y = bird_y - 50
    if new_event.type == KEYDOWN and new_event.key == K_DOWN:
        bird_y = bird_y + 50

    for pipe in pipes:
        pipe.move()

    #Move the coin
    coin.move()


    background = screen.blit(background_image, (0, 0))
    bird = screen.blit(bird_image, (bird_x, bird_y))

    for pipe in pipes:
        pipe.blit()

    #Blit the coin
    coin.blit()
        
    display.update()

    for pipe in pipes:
        if pipe.collides_with(bird):
            print("Game Over!")
            quit()
            over = True
            break
        
    #Check if the coin is collected and update the points
    if coin.collected_by(bird):
        points = points + 1

    if over:
        break

#Print out our point total at the end
print("Points:", points)
