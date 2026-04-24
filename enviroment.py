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