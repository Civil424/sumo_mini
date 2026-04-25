import enviroment as en
import vehicles
import pygame as pg
import math

def run_app(screen):
    rt_ed = False
    first_node = None
    run = True
    while run:
        screen.fill((0,0,0))
        # roads rendering
        for start, end in en.roads:
            pg.draw.line(screen, (120,120,120), en.nodes[start], en.nodes[end], 12)
        # nodes rendering
        if rt_ed == True:
            for nod in en.nodes.values():
                pg.draw.circle(screen, "red", nod, 8)

        pg.display.update()

        for event in pg.event.get():

            if event.type == pg.MOUSEBUTTONDOWN:
                # route editing mode
                if event.button == 3 and rt_ed == False:
                    rt_ed = True
                elif event.button == 3:
                    rt_ed = False

                # routes & nodes creating
                if event.button == 1 and rt_ed == True:
                    mouse_pos = pg.mouse.get_pos()

                    if first_node == None:
                        first_node = mouse_pos
                    else:
                        second_node = mouse_pos
                        en.create_road(first_node, second_node)
                        first_node = None

            if event.type == pg.QUIT:
                print(en.nodes)
                print(en.roads)
                run = False

pg.quit()