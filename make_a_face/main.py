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
    no_stroke()
    # rambut
    fill(0,0,0)
    ellipse(200,180,300,300)

    # wajah
    fill(128,128,128)
    ellipse(200-75,180+10,300-150,300-100)

    fill(128,128,128)
    ellipse(200+75,180+10,300-150,300-100)

    fill(128,128,128)
    ellipse(200,180+75,230,150)

    fill(128,128,128)
    rect(200,210,100,100)

    # mata
    fill(0,0,0)
    ellipse(200-70,210,50,50)
    fill(255,255,255)
    ellipse(200-60,210-10,20,20)
    
    fill(0,0,0)
    ellipse(200+70,210,50,50)
    fill(255,255,255)
    ellipse(200+80,210-10,20,20)

    fill(128,128,128)
    ellipse(200-70,210+30,50,50)

    fill(128,128,128)
    ellipse(200+70,210+30,50,50)

    # mulut
    fill(0,0,0)
    rect(200,200+80,100,10)

    fill(0,0,0)
    triangle(
        100,0,
        100,0,
        100,0
    )

# Keep this to run your code
run()
