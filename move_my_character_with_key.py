from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('run.png')

face = 0
dirx = 0
diry = 0
x = 800//2
y = 400//2
frame = 0
running = True

def handle_events():
    global face
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            pass
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_DOWN:
                face = 1
            elif event.key == SDLK_LEFT:
                face = 2
            elif event.key == SDLK_UP:
                face = 0
            elif event.key == SDLK_RIGHT:
                face = 3
        elif event.type == SDL_KEYUP:
            pass

def draw_character():
    global frame,x,y
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(32 + (frame * 80),32 + (face * 80),16,16,x,y,80,80)
    update_canvas()
    frame = (frame + 1) % 8

def move_character():
    global x,y
    x += dirx * 5
    y += diry * 5

while running:
    draw_character()
    handle_events()
    delay(0.05)



close_canvas()

