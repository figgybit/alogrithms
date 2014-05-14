# import AVLTree3
# tree = AVLTree3.AVLTree(10)
# tree.add(2)
# tree.add(3)
# tree.add(4)
# tree.add(6)
# tree.add(7)
# tree.add(5)
# tree.add(9)
# tree.add(10)
# tree.add(14)
# tree.add(12)
# tree.add(13)
# tree.add(11)
# tree.add(15)
# tree.print_tree()
# if 1:
#   for x in range(29):
#     tree.add(x)
#   for x in range(100):
#     tree.add(x)
#   for x in range(100):
#     tree.add(x)
#   tree.print_tree()



from PIL import Image, ImageDraw, ImageFont

class Node():
  def __init__(self, value=None, parent=None, left=None, right=None):
    self.value = value
    self.parent = parent
    self.left = left
    self.right = right
    self.level = 0
    self.balance_factor = 0


class AVLTree():

  def __init__(self, value):
    self.root = Node(value)

  def inorder_iter(self):
    stack = [[self.root, None]]
    while stack:
      node, direction = stack.pop()
      if direction == None:
        stack.append([node, "left"])
        while (node.left):
          node = node.left
          stack.append([node, "left"])
      elif direction == "left":
        print node.value
        node = node.right
        if node:
          stack.append([node, "left"])
          while (node.left):
            node = node.left
            stack.append([node, "left"])

  def preorder_iter(self):
    stack = [self.root]
    while stack:
      node = stack.pop()
      print node.value
      if node.right:
        stack.append(node.right)
      if node.left:
        stack.append(node.left)

  def postorder_iter(self):
    stack = [[self.root, None]]
    while stack:
      node, direction = stack.pop()
      if direction == None:
        stack.append([node, "left"])
        while (node.left):
          node = node.left
          stack.append([node, "left"])
      elif direction == "left":
        stack.append([node, "right"])
        if node.right:
          node = node.right
          stack.append([node, "left"])
          while node.left:
            node = node.left
            stack.append([node, "left"])
      elif direction == "right":
        print node.value

  def preorder(self, node):
      if not node:
        return
      print node.value
      self.preorder(node.left)
      self.preorder(node.right)

  def inorder(self, node):
      if not node:
        return
      self.inorder(node.left)
      print '{0} - {1} - {2}'.format(node.value, node.level, node.balance_factor)
      self.inorder(node.right)

  def postorder(self, node):
    if not node:
      return
    self.postorder(node.left)
    self.postorder(node.right)
    print node.value

  def delete(self, node):
    if node.left:
      replacement = node.left
      while replacement.right:
        replacement = replacement.right
      while replacement.parent != node:
        self.right_times(replacement)
      if node.right:
        replacement.right = node.right
        node.right.parent = replacement
      if node == self.root:
        self.root = replacement
      replacement.parent = node.parent
      if node.parent:
        if node.parent.left == node:
          node.parent.left = replacement
        elif node.parent.right == node:
          node.parent.right = replacement
      node = replacement.left
      while node.right:
        node = node.right
      self.recalculate_balance_factor(node)
    elif node.right:
      replacement = node.right
      while replacement.left:
        replacement = replacement.left
      while replacement.parent != node:
        self.left_times(replacement)
      if node.left:
        replacement.left = node.left
        node.left.parent = replacement
      if node == self.root:
        self.root = replacement
      replacement.parent = node.parent
      if node.parent:
        if node.parent.right:
          node.parent.right = replacement
        elif node.parent.left == node:
          node.parent.left = replacement
      node = replacement.right
      while node.left:
        node = node.left
      self.recalculate_balance_factor(node)
    else:
      if node.parent.left == node:
        node.parent.left = None
      elif node.parent.right == node:
        node.parent.right = None
      else:
        self.root = None
      del node

  def find_position(self, node, value):
    while (node):
      if node.value > value:
        if node.left:
          node = node.left
        else:
          return [node, "left"]
      else:
        if node.right:
          node = node.right
        else:
          return [node, "right"]

  def add(self, value, rebalance=True):
    node, position = self.find_position(self.root, value)
    new_node = Node(value)
    if position == "left":
      new_node.parent = node
      node.left = new_node
    else:
      new_node.parent = node
      node.right = new_node
    self.recalculate_balance_factor(node)

  def rebalance(self, node):
      if node.balance_factor == 2:
        node = node.left
        if node.balance_factor <= -1:
          self.left_right(node)
        elif node.balance_factor >= 0:
          self.left_left(node)
        else:
          self.rebalance(node)
      if node.balance_factor == -2:
        node = node.right
        if node.balance_factor <= 0:
          self.right_right(node)
        elif node.balance_factor >= 1:
          self.right_left(node)
        else:
          self.rebalance(node)

  def right_times(self, node):
    parent = node.parent
    if node.parent.right and node.parent.right == node:
      left_child = node.left
      grand_parent = parent.parent
      if grand_parent:
        if grand_parent.right == parent:
          grand_parent.right = node
          node.parent = grand_parent
        else:
          grand_parent.left = node
          node.parent = grand_parent
      else:
        self.root = node
        node.parent = None
      node.left = parent
      parent.parent = node
      if left_child:
        parent.right = left_child
        left_child.parent = parent
      else:
        parent.right = None

  def left_times(self, node):
    parent = node.parent
    if node.parent.left and node.parent.left == node:
      right_child = node.right
      grand_parent = parent.parent
      if grand_parent:
        if grand_parent.right == parent:
          grand_parent.right = node
          node.parent = grand_parent
        else:
          grand_parent.left = node
          node.parent = grand_parent
      else:
        self.root = node
        node.parent = None
      node.right = parent
      parent.parent = node
      if right_child:
        parent.left = right_child
        right_child.parent = parent
      else:
        parent.left = None

  def left_right(self, node):
    node = node.right
    self.right_times(node)
    self.left_times(node)
    self.recalculate_balance_factor(node)

  def right_left(self, node):
    node = node.left
    self.left_times(node)
    self.right_times(node)
    self.recalculate_balance_factor(node)

  def left_left(self, node):
    self.left_times(node)
    self.recalculate_balance_factor(node)

  def right_right(self, node):
    self.right_times(node)
    self.recalculate_balance_factor(node)

  def set_balance_factor(self, node):
    left_level = 1
    right_level = 1
    if node.left:
      left_level = node.left.level + 1
    if node.right:
      right_level = node.right.level + 1
    node.level = max(right_level, left_level)
    node.balance_factor = left_level - right_level
    if node.balance_factor >= 2 or node.balance_factor <= -2:
      self.rebalance(node)

  def recalculate_balance_factor(self, start):
    if start.left:
      node = start.left
      self.set_balance_factor(node)
    if start.right:
      node = start.right
      self.set_balance_factor(node)
    node = start
    self.set_balance_factor(node)
    while (node.parent):
      node = node.parent
      self.set_balance_factor(node)

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
      text_pos = (mid-10,height-10)
      draw.text(text_pos, str(node.balance_factor), fill=red, font=font)
      text_pos = (mid+50,height+50)
      draw.text(text_pos, str(node.level), fill=red, font=font)
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



