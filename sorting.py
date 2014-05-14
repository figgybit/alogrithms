
class QuickSort():
  # q = QuickSort([101, 10,1,7,4,10,22,15,3,6,8,100,14,16,15,2])
  def __init__(self, values=[]):
    self.array = values
    self.sort(0, len(self.array))
  def sort(self, start, end):
    sortvalue = self.array[start]
    index = start+1
    iterator = start+1
    while iterator < end:
      if self.array[iterator] < sortvalue:
        x = self.array[index]
        self.array[index] = self.array[iterator]
        self.array[iterator] = x
        index += 1
      iterator+=1
    x = self.array[index-1]
    self.array[index-1] = self.array[start]
    self.array[start] = x
    if start < index-1:
      self.sort(start, index)
    if index < end:
      self.sort(index, end)



class MergeSort():
  # q = MergeSort([101, 10,1,7,4,10,22,15,3,6,8,100,14,16,15])
  def __init__(self, values=[]):
    self.array = self.sort(values)
  def sort(self, list_to_sort):
    if len(list_to_sort) == 1:
      return list_to_sort
    list1 = self.sort(list_to_sort[0:len(list_to_sort)/2])
    list2 = self.sort(list_to_sort[(len(list_to_sort)/2):])
    lengeth = len(list1)+len(list2)
    list1.append(float("inf"))
    list2.append(float("inf"))
    merged_list = []
    list1_index = 0
    list2_index = 0
    for x in range(lengeth):
      if list1[list1_index] < list2[list2_index]:
        merged_list.append(list1[list1_index])
        list1_index += 1
      else:
        merged_list.append(list2[list2_index])
        list2_index += 1
    return merged_list