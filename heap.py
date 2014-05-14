
class OneListMax(list):
  def __getitem__(self, index):
    if len(self) < index:
      return float("-inf")
    if index == 0:
      return float("inf")
    return list.__getitem__(self, index-1)
  def __setitem__(self, index, value):
    return list.__setitem__(self, index-1, value)


class OneListMin(list):
  def __getitem__(self, index):
    if len(self) < index:
      return float("inf")
    if index == 0:
      return float("-inf")
    return list.__getitem__(self, index-1)
  def __setitem__(self, index, value):
    return list.__setitem__(self, index-1, value)


class Heap():
  # h = Heap('max', [1,7,4,10,22,15,3,6,8,100,14,16,15])
  # h = Heap('min', [1,7,4,10,22,15,3,6,8,100,14,16,15])
  def __init__(self, type, value=[]):
    if type == 'min':
      self.root = OneListMin(value)
      self.get_best = lambda x,y : min (x,y)
      self.execute = lambda x,y : x < y
    else:
      self.root = OneListMax(value)
      self.get_best = lambda x,y : max (x,y)
      self.execute = lambda x,y : x > y
    self.heapify()
  def heapify_up(self, index):
    if self.execute (self.root[index], self.root[ index/2 ]):
      x = self.root[ index/2 ]
      self.root[ index/2 ] = self.root[index]
      self.root[index] = x
      index = index/2
      self.heapify_up(index)
  def add(self, value):
    self.root.append(value)
    index = len(self.root)
    self.heapify_up(index)
  def heapify_down(self, index):
    max_child = self.get_best(self.root[2*index],  self.root[(2*index)+1])
    if self.execute (max_child, self.root[index] ):
      if max_child == self.root[2*index]:
        x = self.root[2*index]
        self.root[2*index] = self.root[index]
        self.root[index] = x
        self.heapify_down(2*index)
      else:
        x = self.root[(2*index)+1]
        self.root[(2*index)+1] = self.root[index]
        self.root[index] = x
        self.heapify_down((2*index)+1)
  def pop(self):
    if self.root:
      if len(self.root) == 1:
        return self.root.pop()
      if self.root:
        x = self.root.pop()
        max_value = self.root[1]
        self.root[1] = x
        self.heapify_down(1)
        return max_value
  def heapify(self):
    for x in range(len(self.root), -1, -1):
      self.heapify_down(x)
  def heap_sort(self):
    size = range(len(self.root), -1, -1)
    self.sortlist = []
    for x in size:
      if x > 0:
        self.sortlist.append(self.pop())

