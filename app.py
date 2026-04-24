import enviroment as en
import vehicles
import pygame as pg

def run_app(screen):
    rt_ed = False
    first_node = None
    run = True
    while run:
        screen.fill((0,0,0))

        for start, end in en.roads:
            pg.draw.line(screen, (120,120,120), en.nodes[start], en.nodes[end], 12)

        pg.display.update()

        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 3 and rt_ed == False:
                    rt_ed = True
                elif event.button == 3:
                    rt_ed = False

                if event.button == 1 and rt_ed == True:
                    if first_node == None:
                        first_node = pg.mouse.get_pos()
                    else:
                        second_node = pg.mouse.get_pos()
                        create_road(first_node, second_node)
                        first_node = None

            if event.type == pg.QUIT:
                run = False

def create_road(first_node,second_node):
    start = en.node_id
    en.node_id += 1
    end = en.node_id
    en.node_id += 1

    en.nodes[start] = (first_node)
    en.nodes[end] = (second_node)
    en.roads.append((start,end))
pg.quit()