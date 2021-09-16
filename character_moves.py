from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

while(True):
    x = 50
    while x < 750:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 90)
        x += 5
        delay(0.003)

    y = 90
    while y < 550:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(750, y)
        y += 5
        delay(0.003)

    while x > 50:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 550)
        x -= 5
        delay(0.003)

    while y > 90:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(50, y)
        y -= 5
        delay(0.003)

    z = 0
    while z < 6.3:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(400 + 250*math.cos(z), 300 + 250*math.sin(z))
        z += 0.05
        delay(0.01)
    
close_canvas()