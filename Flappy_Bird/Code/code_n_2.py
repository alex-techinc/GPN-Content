from pygame import *
from random import *

#Moved init and images above the class
init()

background_image = image.load("bg.png")
bird_image = image.load("bird.png")
pipe_image = image.load("pipe.png")
flipped_pipe_image = transform.flip(pipe_image, False, True)

class Pipe ():
    def __init__(self, x, y, flipped):
        self.x = x
        self.y = y
        self.flipped = flipped

    #Added blit function
    def blit(self):
        if self.flipped:
            self.rect = screen.blit(flipped_pipe_image, (self.x, -self.y))
        else:
            self.rect = screen.blit(pipe_image, (self.x, self.y))


print("The game is about to start!")

screen = display.set_mode((800, 600))

bird_x = 10
bird_y = 250

pipe1_object = Pipe(200, 250, False)
pipe2_object = Pipe(450, 100, False)
pipe3_object = Pipe(700, 400, True)

while True:
    new_event = event.poll()
    if new_event.type == KEYDOWN and new_event.key == K_UP:
        bird_y = bird_y - 50
    if new_event.type == KEYDOWN and new_event.key == K_DOWN:
        bird_y = bird_y + 50
        
    pipe1_object.x = pipe1_object.x - 2
    pipe2_object.x = pipe2_object.x - 2
    pipe3_object.x = pipe3_object.x - 2

    background = screen.blit(background_image, (0, 0))
    bird = screen.blit(bird_image, (bird_x, bird_y))

    #Use the blit function instead
    pipe1_object.blit()
    pipe2_object.blit()
    pipe3_object.blit()
        
    display.update()

    #Update to use class
    if bird.colliderect(pipe1_object.rect):
        print("Game Over!")
        quit()
        break

    #Update to use class
    if bird.colliderect(pipe2_object.rect):
        print("Game Over!")
        quit()
        break

    #Update to use class
    if bird.colliderect(pipe3_object.rect):
        print("Game Over!")
        quit()
        break

    if pipe1_object.x < -50:
        pipe1_object.x = 800
        pipe1_object.y = randint(100, 500)
        pipe1_object.flipped = choice([True, False])
        
    if pipe2_object.x < -50:
        pipe2_object.x = 800
        pipe2_object.y = randint(100, 500)
        pipe2_object.flipped = choice([True, False])

    if pipe3_object.x < -50:
        pipe3_object.x = 800
        pipe3_object.y = randint(100, 500)
        pipe3_object.flipped = choice([True, False])
