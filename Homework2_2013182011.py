from pico2d import *
import math

def handle_events():
    global running
    global x,y
    global r
    global center_x,center_y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                center_x = center_x + 10
            elif event.key == SDLK_LEFT:
                center_x = center_x - 10
            elif event.key == SDLK_UP:
                center_y = center_y + 10
            elif event.key == SDLK_DOWN:
                center_y = center_y - 10
            elif event.key == SDLK_a:
                r = r+ 10
                if r>=300:
                    r = r - 10
            elif event.key == SDLK_d:
                r = r - 10
                if r<=20:
                    r = r+10
center_x = 300
center_y = 300
r = 100
angle = 1
open_canvas()
grass = load_image('grass.png')
character = load_image('run_animation.png')
x = math.cos(angle) * r + center_x
y = math.sin(angle) * r + center_y
running = True
frame = 0
while (running):
    clear_canvas()
    grass.draw(400, 30)
    x = math.cos(angle) * r + center_x
    y = math.sin(angle) * r + center_y
    character.clip_draw(frame * 100, 0, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8
    angle = angle + 1
    delay(0.05)
    handle_events()

close_canvas()

