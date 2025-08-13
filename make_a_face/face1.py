from p5 import *

screen_size = 400


def setup():
    # Put code to run once here
    size(screen_size, screen_size)
    rect_mode(CENTER)


def draw():
    # Put code to run every frame here
    background(255, 255, 255)
    # Add code to draw your face here
    fill(0,128,255)
    no_stroke()
    ellipse(200,200,300,300)
    fill(255,0,0)
    ellipse(80,200,70,70)
    fill(255,0,0)
    ellipse(320,200,70,70)
    fill(255,0,0)
    rect(200,200,250,60)
    fill(0,0,0)
    ellipse(200-65,200,40,40)
    fill(0,0,0)
    ellipse(200+65,200,40,40)

    

# Keep this to run your code
run()
