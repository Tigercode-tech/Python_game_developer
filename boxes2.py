import pgzrun
from random import randint
WIDTH = 300
HEIGHT = 300
def draw():
    r=255
    g=randint(120,255)
    b=0
    width=WIDTH
    height=HEIGHT-200
    for i in range(20):
        rect=Rect((0,0),(width,height))
        rect.center=150,150
        screen.draw.rect(rect,(r,g,b))
        b+=10
        r-=10
        width-=5
        height+=9
pgzrun.go()