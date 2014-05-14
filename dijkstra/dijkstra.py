# GRAPH = {
#   1: [[2,7], [3,9], [6,14]],
#   2: [[1,7], [3,10], [4,15]],
#   6: [[1,14], [3,2], [5,9]],
#   3: [[6,2], [4,11], [2,10], [1,9]],
#   4: [[2,15], [3,11], [5,6]],
#   5: [[6,9], [4,6]],
#   7: [],
#   8: [],
#   9: [],
#   10: [],
#   11: [],
#   12: [],
#   13: [],
#   14: [],
#   15: []
# }
# g = Graph(GRAPH)
# one = g.nodes[1]
# end = g.nodes[5]
# d = Dijkstra(g, one, end)
# self = d

from PIL import Image, ImageDraw, ImageFont

class Node():
  def __init__(self, value):
    self.value = value
    self.children = None
    self.parent = None
    self.height = 1
    self.marked = False
    self.left = self
    self.right = self
    self.distance = float('inf')
    self.pathes = []

class Graph():
  def __init__(self, graph):
    self.nodes = dict()
    for n in graph:
      self.nodes[n] = Node(n)
    for n in graph:
      for node, cost in graph[n]:
        self.nodes[n].pathes.append([self.nodes[node], cost])

class LinkedList():
  def __init__(self, node):
    self.start = node
    self.end = node
  def add(self, node):
    if self.end == None and self.start == None:
      self.start = node
      self.end = node
    else:
      self.end.right = node
      node.left = self.end
      self.end = node
      self.start.left = node
      node.right = self.start
  def disconnect(self, node):
    if node == self.start and node == self.end:
      self.end = None
      self.start = None
    else:
      if node == self.start:
        self.start = node.right
      if node == self.end:
        self.end = node.left
      right = node.right
      left = node.left
      right.left = left
      left.right = right
      node.right = node
      node.left = node
  def contains(self, node):
    for n in self:
      if n == node:
        return True
    return False
  def get_list_of_nodes(self, node):
    nodes = []
    for n in self:
      nodes.append(n)
    return nodes
  def __iter__(self):
    self.current = None
    return self
  def next(self):
    if self.current == self.start:
      self.current = None
      raise StopIteration
    else:
      if self.current:
        node = self.current
        self.current = self.current.right
        return node
      else:
        self.current = self.start.right
        return self.start

class Dijkstra():
  def __init__(self, graph, start_node, end_node):
    self.minimum = None
    self.root_list = None
    self.graph = graph
    self.start_node = start_node
    self.end_node = end_node
    self.accounted = []
    for node in graph.nodes:
      if graph.nodes[node] != self.start_node:
        if not self.root_list:
          self.root_list = LinkedList(graph.nodes[node])
        else:
          self.root_list.add(graph.nodes[node])
    self.balance_heap()
    self.find_path()
  def get_new_height(self, node):
    max_height = 1
    if node.children:
      for n in node.children:
        if n.height + 1 > max_height:
          max_height = n.height + 1
    node.height = max_height
    if node.parent:
      self.get_new_height(node.parent)
  def decrement_cost(self, current_distance, nodes):
    for node, cost in nodes:
      if node not in self.accounted:
        if node.distance > cost+current_distance:
          node.distance = cost+current_distance
          if not self.root_list.contains(node):
            node.marked = True
            while node and node.marked:
              if node.parent:
                node.parent.children.disconnect(node)
                self.root_list.add(node)
                self.get_new_height(node)
              node.marked = False
              parent = node.parent
              node.parent = None
              node = parent
            if node:
              self.get_new_height(node)
              if not self.root_list.contains(node):
                node.marked = True
  def find_min(self):
    for node in self.root_list:
      if node.distance < self.minimum.distance:
        self.minimum = node
    if self.end_node.distance == self.minimum.distance:
      self.minimum = self.end_node
    node = self.minimum
    if node.children:
      while node.children.start:
        n = node.children.start
        print n.value
        node.children.disconnect(n)
        self.root_list.add(n)
        self.get_new_height(n)
        n.parent = None
    self.root_list.disconnect(node)
    self.minimum = None
    # self.balance_heap()
    return node
  def find_path(self):
    node = self.start_node
    self.accounted.append(node)
    node.distance = 0
    i = 1
    while self.end_node not in self.accounted:
      self.decrement_cost(node.distance, node.pathes)
      self.balance_heap()
      node = self.find_min()
      self.balance_heap()
      self.print_tree(i)
      i+=1
      self.accounted.append(node)
  def merge_roots(self, node1, node2):
    if node1.distance < node2.distance:
      self.root_list.disconnect(node2)
      if not node1.children:
        node1.children = LinkedList(node2)
      else:
        node1.children.add(node2)
      node2.parent = node1
      node1.height += 1
      return node1
    else:
      self.root_list.disconnect(node1)
      if not node2.children:
        node2.children = LinkedList(node1)
      else:
        node2.children.add(node1)
      node1.parent = node2
      node2.height += 1
      return node2
  def balance_heap(self):
    self.tmp = {}
    for node in self.root_list:
      print node
      if node.height in self.tmp:
        while (node.height in self.tmp):
          print node.height
          print self.tmp
          node1 = self.tmp[node.height]
          del self.tmp[node.height]
          node = self.merge_roots(node1, node)
        self.tmp[node.height] = node
      else:
        self.tmp[node.height] = node
    for node in self.root_list:
      if not self.minimum or self.minimum.distance > node.distance:
        self.minimum = node
  def preorder_print(self, draw):
    level = 0
    width = 100
    stack = []
    for node in self.root_list:
      stack.append([node, level, width])
      width += 500
    red = (255,0,0)
    green = (0,255,0)
    font = ImageFont.truetype( 'arial.ttf', 20 )
    while (stack):
      node, level, width = stack.pop()
      height = (level*55) + 30
      if not node.marked:
        draw.ellipse((width, height, width+50, height+50), fill=green)
      else:
        draw.ellipse((width, height, width+50, height+50))
      text_pos = (width+50,height)
      draw.text(text_pos, str(node.value), fill=red, font=font)
      text_pos = (width+15,height+10)
      draw.text(text_pos, str(node.height), fill=red, font=font)
      text_pos = (width,height)
      draw.text(text_pos, str(node.distance), fill=red, font=font)
      level += 1
      if node.children:
        for n in node.children:
          stack.append([n, level, width])
          width += 75
  def print_tree(self, i=0):
    width = 2500
    size = (width,1000)
    im = Image.new('RGB', size)
    draw = ImageDraw.Draw(im)
    self.preorder_print(draw)
    del draw
    im.save('image{0}.PNG'.format(i))

