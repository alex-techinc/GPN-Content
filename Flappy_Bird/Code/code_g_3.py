from pygame import *
init()

print("The game is about to start!")

screen = display.set_mode((800, 600))

background_image = image.load("bg.png")
bird_image = image.load("bird.png")
pipe_image = image.load("pipe.png")

#Added bird coordinates
bird_x = 10
bird_y = 250

#Added pipes coordinates
pipe_x = 200
pipe_y = 250
pipe2_x = 450
pipe2_y = 100
pipe3_x = 700
pipe3_y = 400

background = screen.blit(background_image, (0, 0))
#Blit the bird and the pipes
bird = screen.blit(bird_image, (bird_x, bird_y))
pipe = screen.blit(pipe_image, (pipe_x, pipe_y))
pipe2 = screen.blit(pipe_image, (pipe2_x, pipe2_y))
pipe3 = screen.blit(pipe_image, (pipe3_x, pipe3_y))

display.update()
