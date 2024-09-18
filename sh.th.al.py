import pgzrun
from random import randint
TITLE='SHOOT THE ALIEN'
WIDTH=500
HEIGHT=500
message='HELP, ALIENS!'
alien=Actor('alien')
def draw():
    screen.clear
    screen.fill(color=(90,254,9))
    alien.draw()
    screen.draw.text(message,center=(480,18),fontsize=38)
def place_alien():
    alien.x=randint(58,WIDTH-50)
    alien.y=randint(58,HEIGHT-50)
def on_mouse_down(pos):
    global message
    if alien.collidepoint(pos):
        message='Good Scratch on the body'
        place_alien()
    else:
        message='NO'
place_alien()
pgzrun.go()
