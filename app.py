import enviroment as en
import vehicles
import pygame as pg
import math

def run_app(screen):
    rt_ed = False
    first_node = None
    run = True
    move_mode = False
    near_node_move = None
    font = pg.font.Font(None,36)
    while run:

        screen.fill((0, 0, 0))
        # roads rendering
        for road in en.roads.values():
            pg.draw.line(screen, (120, 120, 120), en.nodes[road.start], en.nodes[road.end], 12)
        # nodes rendering
        if rt_ed == True:
            for nod in en.nodes.values():
                pg.draw.circle(screen, "red", nod, 8)

        current_mouse_pos = pg.mouse.get_pos()

        pg.display.update()

        for event in pg.event.get():
            keys = pg.key.get_pressed()

            if event.type == pg.MOUSEBUTTONDOWN:
                # route editing mode
                if event.button == 3 and rt_ed == False:
                    rt_ed = True
                elif event.button == 3:
                    rt_ed = False

                # near node for moving
                if keys[pg.K_LSHIFT]:
                    near_node_move = en.nearest_node(current_mouse_pos)

                # routes & nodes creating
                elif event.button == 1 and rt_ed == True and move_mode == False:
                    if first_node == None:
                        first_node = current_mouse_pos
                    else:
                        second_node = current_mouse_pos
                        en.create_road(first_node, second_node)
                        first_node = None

            #node moving
            if event.type == pg.MOUSEMOTION:
                if event.buttons[0] and keys[pg.K_LSHIFT]:
                    if near_node_move != None:
                        move_mode = True
                    if move_mode == True:
                        en.move_node(near_node_move,current_mouse_pos)
                        first_node = None
            # if 2 nodes near
            if event.type == pg.MOUSEBUTTONUP:
                node_for_combining = en.search_near_node(near_node_move)
                if node_for_combining != None and near_node_move != node_for_combining:
                    print("Желаете ли вы объеденить ноды? (Y–yes, N-no)")
                    i = (input())
                    if i == "Y":
                        en.combining_nodes(near_node_move,node_for_combining)
                    elif i == "N":
                        move_mode = False
            else:
                move_mode = False

            if event.type == pg.QUIT:
                print("Nodes:",en.nodes)
                print("Roads",en.roads)
                run = False

pg.quit()