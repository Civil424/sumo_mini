import math

class Node:
    def __init__(self,xcord,ycord):
        self.xcord = xcord
        self.ycord = ycord

class Road:
    def __init__(self,start,end,oneside,lines,width,mspd):
        self.start = start
        self.end = end
        self.oneside = oneside
        self.lines = lines
        self.wigth = width
        self.mspd = mspd

class Bulding:
    def __init__(self,width,length):
        self.width = width
        self.length = length

nodes = {}
roads = []
node_id = 1

def nearest_node(mouse_pos):
    nearest_node_id = None
    nearest_dist = 8
    for node_id,node_cords in nodes.items():
        dx = mouse_pos[0] - node_cords[0]
        dy = mouse_pos[1] - node_cords[1]
        dist = math.hypot(dx,dy)
        if dist < nearest_dist:
            nearest_dist = dist
            nearest_node_id = node_id
    return nearest_node_id

def create_node(coords):
    global node_id
    node = node_id
    nodes[node] = (coords)
    node_id += 1
    return node

def create_road(first_node,second_node):
    near_first = nearest_node(first_node)
    near_second = nearest_node(second_node)

    if near_first != None:
        start = near_first
    else:
        start = create_node(first_node)
    if near_second != None:
        end = near_second
    else:
        end = create_node(second_node)
    roads.append((start,end))