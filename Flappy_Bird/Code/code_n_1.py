from pygame import *
from random import *

#Made a new pipe class
class Pipe ():
    def __init__(self, x, y, flipped):
        self.x = x
        self.y = y
        self.flipped = flipped

init()

print("The game is about to start!")

screen = display.set_mode((800, 600))

background_image = image.load("bg.png")
bird_image = image.load("bird.png")
pipe_image = image.load("pipe.png")
flipped_pipe_image = transform.flip(pipe_image, False, True)

bird_x = 10
bird_y = 250

#Converted variables into the class
pipe1_object = Pipe(200, 250, False)
pipe2_object = Pipe(450, 100, False)
pipe3_object = Pipe(700, 400, True)

while True:

    new_event = event.poll()
    if new_event.type == KEYDOWN and new_event.key == K_UP:
        bird_y = bird_y - 50
    if new_event.type == KEYDOWN and new_event.key == K_DOWN:
        bird_y = bird_y + 50

    #Updated to use the class
    pipe1_object.x = pipe1_object.x - 2
    pipe2_object.x = pipe2_object.x - 2
    pipe3_object.x = pipe3_object.x - 2

    background = screen.blit(background_image, (0, 0))
    bird = screen.blit(bird_image, (bird_x, bird_y))

    #Updated to use the class
    if pipe1_object.flipped:
        pipe = screen.blit(flipped_pipe_image, (pipe1_object.x, -pipe1_object.y))
    else:
        pipe = screen.blit(pipe_image, (pipe1_object.x, pipe1_object.y))
    if pipe2_object.flipped:
        pipe2 = screen.blit(flipped_pipe_image, (pipe2_object.x, -pipe2_object.y))
    else:
        pipe2 = screen.blit(pipe_image, (pipe2_object.x, pipe2_object.y))
    if pipe3_object.flipped:
        pipe3 = screen.blit(flipped_pipe_image, (pipe3_object.x, -pipe3_object.y))
    else:
        pipe3 = screen.blit(pipe_image, (pipe3_object.x, pipe3_object.y))
        
    display.update()

    if bird.colliderect(pipe):
        print("Game Over!")
        quit()
        break

    if bird.colliderect(pipe2):
        print("Game Over!")
        quit()
        break
    
    if bird.colliderect(pipe3):
        print("Game Over!")
        quit()
        break
    
    #Updated to use the class
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
