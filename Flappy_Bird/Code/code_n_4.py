from pygame import *
from random import *

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


print("The game is about to start!")

screen = display.set_mode((800, 600))

bird_x = 10
bird_y = 250

pipe1_object = Pipe(200, 250, False)
pipe2_object = Pipe(450, 100, False)
pipe3_object = Pipe(700, 400, True)

#Added a list of the pipes
pipes = [pipe1_object, pipe2_object, pipe3_object]

#Added over variable
over = False

while True:

    new_event = event.poll()
    if new_event.type == KEYDOWN and new_event.key == K_UP:
        bird_y = bird_y - 50
    if new_event.type == KEYDOWN and new_event.key == K_DOWN:
        bird_y = bird_y + 50

    #Using a loop for this now
    for pipe in pipes:
        pipe.move()

    background = screen.blit(background_image, (0, 0))
    bird = screen.blit(bird_image, (bird_x, bird_y))

    #Using a loop for this now
    for pipe in pipes:
        pipe.blit()
        
    display.update()

    #Using a loop for this now
    for pipe in pipes:
        if pipe.collides_with(bird):
            print("Game Over!")
            #Don't forget to set over to true
            over = True
            quit()
            break

    #When the game is over we need to break the big while loop
    if over:
        break

