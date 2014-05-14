# import SplayTree
# tree = SplayTree.SplayTree(10)
# tree.add(2)
# tree.add(11)
# tree.add(10)
# tree.add(20)
# tree.add(1)
# tree.add(8)
# tree.add(9)
# tree.print_tree()

from PIL import Image, ImageDraw, ImageFont

class Node():
  def __init__(self, value=None, parent=None, left=None, right=None):
    self.value = value
    self.parent = parent
    self.left = left
    self.right = right


class SplayTree():

  def __init__(self, value):
    self.root = Node(value)

  def find_node(self, value, node):
    while node:
      if node.value < value:
        if node.right:
          node = node.right
        else:
          return node, "right"
      else:
        if node.left:
          node = node.left
        else:
          return node, "left"

  def left_times(self, node):
    parent = node.parent
    right = node.right
    if parent != self.root:
      grand_parent = node.parent.parent
      node.parent = grand_parent
      if grand_parent.left == parent:
        grand_parent.left = node
      else:
        grand_parent.right = node
    else:
      self.root = node
      node.parent = None
    node.right = parent
    parent.parent = node
    parent.left = right
    if right:
      right.parent = parent

  def right_times(self, node):
    parent = node.parent
    left = node.left
    if parent != self.root:
      grand_parent = node.parent.parent
      node.parent = grand_parent
      if grand_parent.left == parent:
        grand_parent.left = node
      else:
        grand_parent.right = node
    else:
      self.root = node
      node.parent = None
    node.left = parent
    parent.parent = node
    parent.right = left
    if left:
      left.parent = parent

  def delete(self, node):
    self.splay(node)
    to_delete = node
    right_tree = node.right
    left_tree = node.left
    if right_tree:
      self.root = right_tree
      node = node.right
      while node.left:
        node = node.left
      self.splay(node)
      self.root.left = left_tree
      left_tree.parent = self.root
    else:
      self.root = left_tree
    del to_delete

  def splay(self, node):
    while node != self.root:
      if node.parent.right == node:
        self.right_times(node)
      elif node.parent.left == node:
        self.left_times(node)

  def get(self, value):
    node = self.root
    while node:
      if node.value == value:
        self.splay(node)
        return node
      elif node.value < value:
        if node.right:
          node = node.right
        else:
          return None
      elif node.value > value:
        if node.left:
          node = node.left
        else:
          return None

  def add(self, value):
    node, side = self.find_node(value, self.root)
    new_node = Node(value)
    if side == "left":
      node.left = new_node
      new_node.parent = node
    else:
      node.right = new_node
      new_node.parent = node

  def preorder_print(self, tree, draw, mid):
    level = 0
    stack = [[tree, level, mid]]
    red = (255,0,0)
    font = ImageFont.truetype( 'arial.ttf', 20 )
    while (stack):
      node, level, mid = stack.pop()
      height = (level*55) + 30
      draw.ellipse((mid, height, mid+50, height+50))
      text_pos = (mid+15,height+10)
      draw.text(text_pos, str(node.value), fill=red, font=font)
      level += 1
      leftmid = mid-(1200/(2.3**level))
      rightmid = mid+(1200/(2.3**level))
      if node.right:
        stack.append([node.right, level, rightmid])
      if node.left:
        stack.append([node.left, level, leftmid])

  def print_tree(self):
    width = 2500
    size = (width,1000)
    im = Image.new('RGB', size)
    draw = ImageDraw.Draw(im)
    self.preorder_print(self.root, draw, 1250)
    del draw
    im.save('image.PNG')



