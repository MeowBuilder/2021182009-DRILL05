from pico2d import *

open_canvas()

ground = load_image('ground.png')
character = load_image('character.png')

face = 0
dirx = 0
diry = 0
x = 800//2
y = 400//2
frame = 0
idle_frame = 0
running = True

def handle_events():
    global face,running,dirx,diry,idle_frame
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT or event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_KEYDOWN:
            idle_frame = 0
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
    global idle_frame,frame,x,y
    clear_canvas()
    ground.draw(400, 300)
    if dirx == 0 and diry == 0: #idle상태
        character.clip_draw((idle_frame * 64),(face * 32),64,32,x,y,80,80)
    else:
        character.clip_draw((frame * 32),128 + (face * 32),32,32,x,y,80,80)
    update_canvas()
    idle_frame = (idle_frame + 1) % 4
    frame = (frame + 1) % 8

def move_character():
    global x,y
    if not ((x + dirx * 5) >= 800 or (x + dirx * 5) < 0):
        x += dirx * 5
    if not ((y + diry * 5) >= 600 or (y + diry * 5) < 0):
        y += diry * 5

while running:
    draw_character()
    handle_events()
    move_character()
    if dirx == 0 and diry == 0:
        delay(0.1)
    else:
        delay(0.05)


close_canvas()

