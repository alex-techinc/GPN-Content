from pygame import *
from random import *

init()

print("The game is about to start!")

screen = display.set_mode((800, 600))

background_image = image.load("bg.png")
play_again_image = image.load("play_again.png")
bird_image = image.load("bird.png")
pipe_image = image.load("pipe.png")
flipped_pipe_image = transform.flip(pipe_image, False, True)

bird_x = 10
bird_y = 250

pipe_x = 200
pipe_y = 250
pipe_flipped = False
pipe2_x = 450
pipe2_y = 100
pipe2_flipped = False
pipe3_x = 700
pipe3_y = 400
pipe3_flipped = True

waiting = False
start_time = time.get_ticks()

#Added high score
high_score = 0

while True:
    if waiting:
        screen.blit(play_again_image, (0, 0))
        display.update()
        new_event = event.poll()
        if new_event.type == KEYDOWN and new_event.key == K_q:
            quit()
            break
        if new_event.type == KEYDOWN and new_event.key == K_RETURN:
            bird_x = 10
            bird_y = 250
            pipe_x = 250
            pipe_y = 250
            pipe_flipped = False
            pipe2_x = 500
            pipe2_y = 100
            pipe2_flipped = False
            pipe3_x = 750
            pipe3_y = 400
            pipe3_flipped = True
        
            waiting = False
            start_time = time.get_ticks()
        continue
            

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
    
    if pipe_flipped:
        pipe = screen.blit(flipped_pipe_image, (pipe_x, -pipe_y))
    else:
        pipe = screen.blit(pipe_image, (pipe_x, pipe_y))
    if pipe2_flipped:
        pipe2 = screen.blit(flipped_pipe_image, (pipe2_x, -pipe2_y))
    else:
        pipe2 = screen.blit(pipe_image, (pipe2_x, pipe2_y))
    if pipe3_flipped:
        pipe3 = screen.blit(flipped_pipe_image, (pipe3_x, -pipe3_y))
    else:
        pipe3 = screen.blit(pipe_image, (pipe3_x, pipe3_y))
        
    display.update()

    if bird.colliderect(pipe) or bird.colliderect(pipe2) or bird.colliderect(pipe3):
        print("Game Over!")
        score = (time.get_ticks() - start_time)//1000
        print("You lasted:", score, "seconds!")
        #Added a way to check and update the high score
        if score > high_score:
            high_score = score
            print("You've got a new high score!")
        waiting = True
        

    if pipe_x < -70:
        pipe_x = 800
        pipe_y = randint(100, 500)
        pipe_flipped = choice([True, False])
        
    if pipe2_x < -70:
        pipe2_x = 800
        pipe2_y = randint(100, 500)
        pipe2_flipped = choice([True, False])

    if pipe3_x < -70:
        pipe3_x = 800
        pipe3_y = randint(100, 500)
        pipe3_flipped = choice([True, False])



