from pygame import *
#Added random import
from random import *

init()

print("The game is about to start!")

screen = display.set_mode((800, 600))

background_image = image.load("bg.png")
bird_image = image.load("bird.png")
pipe_image = image.load("pipe.png")
flipped_pipe_image = transform.flip(pipe_image, False, True)

bird_x = 10
bird_y = 250

pipe_x = 200
pipe_y = 250
pipe2_x = 450
pipe2_y = 100
pipe3_x = 700
pipe3_y = 400

while True:
    new_event = event.poll()
    if new_event.type == KEYDOWN and new_event.key == K_UP:
        bird_y = bird_y - 50
    if new_event.type == KEYDOWN and new_event.key == K_DOWN:
        bird_y = bird_y + 50

    pipe_x = pipe_x - 2
    pipe2_x = pipe2_x - 2
    pipe3_x = pipe3_x - 2

    background = screen.blit(background_image, (0, 0))
    bird = screen.blit(bird_image, (bird_x, bird_y))
    pipe = screen.blit(pipe_image, (pipe_x, pipe_y))
    pipe2 = screen.blit(pipe_image, (pipe2_x, pipe2_y))
    pipe3 = screen.blit(flipped_pipe_image, (pipe3_x, -pipe3_y))
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

    #Added ifs to move the pipe back to the start & randomise the y
    if pipe_x < -50:
        pipe_x = 800
        pipe_y = randint(100, 500)
        
    if pipe2_x < -50:
        pipe2_x = 800
        pipe2_y = randint(100, 500)

    if pipe3_x < -50:
        pipe3_x = 800
        pipe3_y = randint(100, 500)
