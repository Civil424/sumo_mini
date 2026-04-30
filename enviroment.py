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

nodes, roads = {}, {}
node_id, road_id = 1, 1

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

def search_near_node(node_id_second):
    second_node_coords = None
    for node_id,node_coords in nodes.items():
        if node_id == node_id_second:
            second_node_coords = node_coords
        elif second_node_coords != None:
            if node_coords[0] - second_node_coords[0] < 8 and node_coords[1] - second_node_coords[1] < 8:
                return node_id
    return None

def create_node(coords):
    global node_id
    node = node_id
    nodes[node] = (coords)
    node_id += 1
    return node

def move_node(drag_node, coords):
    nodes[drag_node] = (coords)

def combining_nodes(node_first, node_second):
    for road in roads.values():
        if road.start == node_first or road.end == node_first:
            if road.start == node_first:
                other_end = road.end
            else:
                other_end = road.start
            if other_end == node_second:
                return
    for road in roads.values():
        if road.start == node_first:
            road.start = node_second
        if road.end == node_first:
            road.end = node_second
    del nodes[node_first]

def create_road(first_node,second_node):
    global road_id
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
    roads[road_id] = Road(start,end,False,2,10,60)
    road_id += 1

def get_road_id(node_id_orig):
    for road_id, node_id in roads.items():
        if node_id.start == node_id_orig or node_id.end == node_id_orig:
            return (road_id, node_id.start, node_id.end)
