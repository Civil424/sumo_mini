
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
    node_for_combining = None
    nodes_combining_memory = None
    waiting_confirm = False
    false_text = False
    font = pg.font.Font(None, 25)

    while run:

        screen.fill((0, 0, 0))
        # roads rendering
        for road in en.roads.values():
            pg.draw.line(screen, (120, 120, 120), en.nodes[road.start].pos(), en.nodes[road.end].pos(), 12)
        # nodes rendering
        if rt_ed == True:
            for nod_id,coords in en.nodes.items():
                pg.draw.circle(screen, "red", coords.pos(), 8)
                text = font.render(str(nod_id), True, (255, 255, 255))
                screen.blit(text,coords.pos())

        current_mouse_pos = pg.mouse.get_pos()
        en.del_duplicate_roads()
        en.cursor_on_road(current_mouse_pos)

        if waiting_confirm == True:
            text = font.render("  Do u want to combining nodes? (Y/N)", True, (255, 255, 255))
            screen.blit(text, current_mouse_pos)
        if false_text == True:
            text = font.render("False operation", True, (255, 255, 255))
            screen.blit(text, current_mouse_pos)

        pg.display.update()

        for event in pg.event.get():
            keys = pg.key.get_pressed()

            if event.type == pg.KEYDOWN:
                # route editing mode
                if event.key == pg.K_RSHIFT and rt_ed == False:
                    rt_ed = True
                    print(" - route ed mode ON")
                elif event.key == pg.K_RSHIFT:
                    rt_ed = False
                    print(" - route ed mode OFF")

                # combining
                if event.key == pg.K_y and waiting_confirm == True:
                    en.combining_nodes(nodes_combining_memory[0],nodes_combining_memory[1])
                    print(" - combine success")
                    waiting_confirm = False
                if event.key == pg.K_n and waiting_confirm == True:
                    move_mode = False
                    nodes_combining_memory = None
                    print(" - combine rejected")
                    waiting_confirm = False

            if event.type == pg.MOUSEBUTTONDOWN:
                # near node for moving
                if keys[pg.K_LSHIFT]:
                    near_node_move = en.nearest_node(current_mouse_pos)
                    first_node = None

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

            # combining nodes
            if event.type == pg.MOUSEBUTTONUP:
                if move_mode == True:
                    node_for_combining = en.search_near_node(near_node_move)
                    if near_node_move == node_for_combining and near_node_move != None:
                        false_text = True
                    elif node_for_combining != None:
                        waiting_confirm = True
                        false_text = False
                        nodes_combining_memory = (near_node_move,node_for_combining)
                        print(" - combine nodes question:",near_node_move,node_for_combining)
                move_mode = False

            # road delete
            # cursor_on = en.cursor_on_road(current_mouse_pos)
            # if cursor_on != None:
            #
            #     en.delete_road(cursor_on)

            if event.type == pg.QUIT:
                print("Nodes:",en.nodes)
                print("Roads",en.roads)
                run = False

pg.quit()