from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('run.png')
idle = load_image('idle.png')

face = 0
dirx = 0
diry = 0
x = 800//2
y = 400//2
frame = 0
running = True

def handle_events():
    global face,running,dirx,diry
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT or event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_DOWN:
                face = 1
                diry -= 1
            elif event.key == SDLK_LEFT:
                face = 2
                dirx -= 1
            elif event.key == SDLK_UP:
                face = 0
                diry += 1
            elif event.key == SDLK_RIGHT:
                face = 3
                dirx += 1
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_DOWN:
                diry += 1
            elif event.key == SDLK_LEFT:
                dirx += 1
            elif event.key == SDLK_UP:
                diry -= 1
            elif event.key == SDLK_RIGHT:
                dirx -= 1

def draw_character():
    global frame,x,y
    clear_canvas()
    grass.draw(400, 30)
    if dirx == 0 and diry == 0: #idle상태
        idle.clip_draw(32 + (frame * 80),32 + (face * 80),16,16,x,y,80,80)
    else:
        character.clip_draw(32 + (frame * 80),32 + (face * 80),16,16,x,y,80,80)
    update_canvas()
    frame = (frame + 1) % 8

def move_character():
    global x,y
    if not ((x + dirx * 5) >= 800 or (x + dirx * 5) < 0):
        x += dirx * 10
    if not ((y + diry * 5) >= 600 or (y + diry * 5) < 0):
        y += diry * 10

while running:
    draw_character()
    handle_events()
    move_character()
    delay(0.05)



close_canvas()

