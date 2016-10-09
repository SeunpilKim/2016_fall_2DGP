import random
from pico2d import *

# Game object class here
class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100,700),90
        self.frame = random.randint(0,7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame +1) %8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
class Ball:
    def __init__(self):
        self.x,self.y = random.randint(0,700),random.randint(400,600)
        self.frame = random.randint(0,20)
        self.image = load_image('ball21x21.png')
        self.fall = True
        self.ycha = random.randint(1,50)
    def update(self):
        self.frame = (self.frame+1) % 8
        if self.fall == True:
            self.y -= self.ycha

    def draw(self):
        self.image.clip_draw(0,0,20,20,self.x,self.y)

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400,30)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
open_canvas()
boy = Boy()
grass = Grass()
ball = Ball()
team = [Boy() for i in range(5)]
balls = [Ball() for i in range(20)]



running = True
# game main loop code
while running:
    handle_events()

    #boy.update()
    for boy in team:
        boy.update()
    for ball in balls:
        ball.update()
        if ball.y <= 60:
            ball.fall = False


    clear_canvas()
    grass.draw()
    #boy.draw()
    for boy in team:
        boy.draw()
    for ball in balls:
        ball.draw()
    update_canvas()
    delay(0.05)

# finalization code

close_canvas()