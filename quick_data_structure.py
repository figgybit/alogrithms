# data structure with fast insertion, removal, membership testing, and random
import random
class QuickData:
  def __init__(self):
    self.quick_list = []
    self.quick_hash = {}
  def add(self, x):
    if x not in self.quick_hash:
      self.quick_list.append(x)
      self.quick_hash[x] = len(self.quick_list) - 1
  def remove(self, x):
    if x in self.quick_hash:
      i = self.quick_hash[x]
      del self.quick_hash[x]
      if len(self.quick_list) == 1:
        self.quick_list = []
      else:
        self.quick_list[i] = self.quick_list[len(self.quick_list) - 1]
        self.quick_hash[self.quick_list[i]] = i
  def member(self, x):
    if x in self.quick_hash:
      return True
    return False
  def random(self):
    r = random.randint(0, len(self.quick_list) - 1)
    return self.quick_list[r]

