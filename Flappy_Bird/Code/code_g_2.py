from pygame import *
init()


print("The game is about to start!")

screen = display.set_mode((800, 600))

#added all the images
background_image = image.load("bg.png")
bird_image = image.load("bird.png")
pipe_image = image.load("pipe.png")

#Blit and display
screen.blit(background_image, (0, 0))
display.update()
