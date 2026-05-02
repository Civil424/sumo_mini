import math

class Node:
    def __init__(self,xcord,ycord,connectedRoads):
        self.xcord = xcord
        self.ycord = ycord
        self.connectedRoads = connectedRoads
    def pos(self):
        return (self.xcord,self.ycord)
    def __repr__(self):
        return f"Node({self.xcord},{self.ycord})"

class Road:
    def __init__(self,start,end,oneside,lines,width,mspd):
        self.start = start
        self.end = end
        self.oneside = oneside
        self.lines = lines
        self.wigth = width
        self.mspd = mspd
    def __repr__(self):
        return f"Road({self.start},{self.end})"

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
        dx = mouse_pos[0] - node_cords.xcord
        dy = mouse_pos[1] - node_cords.ycord
        dist = math.hypot(dx,dy)
        if dist < nearest_dist:
            nearest_dist = dist
            nearest_node_id = node_id
    return nearest_node_id

def search_near_node(node_id_second):
    if node_id_second not in nodes:
        return
    second_node_coords = nodes[node_id_second]
    for node_id,node_coords in nodes.items():
        if node_id == node_id_second:
            continue
        dist = math.hypot(node_coords.xcord - second_node_coords.xcord,node_coords.ycord - second_node_coords.ycord)
        if dist < 10:
            return node_id
    return None

def create_node(coords):
    global node_id
    node = node_id
    nodes[node] = Node(coords[0],coords[1],[])
    node_id += 1
    return node

def move_node(drag_node, coords):
    nodes[drag_node].xcord = coords[0]
    nodes[drag_node].ycord = coords[1]

def combining_nodes(node_first, node_second):
    print(" - combining: node_first=", node_first, "node_second=", node_second)
    for rid, road in roads.items():
        print(" - road", rid, ":", road.start, road.end)
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
    nodes[start].connectedRoads.append(road_id)
    nodes[end].connectedRoads.append(road_id)
    print(" - create road",road_id, ":", start, end)
    road_id += 1

def del_duplicate_roads():
    road_for_del = []
    for road_id, node_id in roads.items():
        road_id_first = road_id
        node_id_first = node_id
        for road_id, node_id in roads.items():
            road_id_second = road_id
            node_id_second = node_id
            if road_id_first != road_id_second and road_id_first not in road_for_del:
                if (node_id_first.start == node_id_second.start and node_id_first.end == node_id_second.end) or \
                        (node_id_first.start == node_id_second.end and node_id_first.end == node_id_second.start):
                    road_for_del.append(road_id_second)
    for road_id in road_for_del:
        del roads[road_id]

def get_road_id(node_id_orig):
    for road_id, node_id in roads.items():
        if node_id.start == node_id_orig or node_id.end == node_id_orig:
            return (road_id, node_id.start, node_id.end)
    return None

def cursor_on_road(mousepos):
    for road_id, node_id in roads.items():
        x1,y1 = nodes[node_id.start].pos()
        x2,y2 = nodes[node_id.end].pos()
        dx = x2 - x1
        dy = y2 - y1
        if dx == 0 and dy == 0:
            continue
        t = ((mousepos[0] - x1) * dx + (mousepos[1] - y1) * dy) / (dx * dx + dy * dy)
        t = max(0, min(1,t))
        nearest_x = x1 + t * dx
        nearest_y = y1 + t * dy
        dist = math.hypot(mousepos[0] - nearest_x, mousepos[1] - nearest_y)
        if dist < 8:
            return road_id
    return None


# def delete_node(node_id_del):


# def delete_road(road_id_del):


