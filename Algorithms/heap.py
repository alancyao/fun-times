class BinaryHeap:
  """ Initializes a list-based binary min heap. """
  def __init__(self, arr=None):
    self.arr = [0]
    self.n = 0
    if arr:
      self.arr += arr
      self.n += len(arr)
      self.heapify()

  def __len__(self):
    return self.n

  def empty(self):
    return self.n == 0

  """ Returns the minimum value of the heap """
  def min(self):
    return self.arr[1] if not self.empty() else None

  def remove_min(self):
    if self.empty():
      return None
    minval = self.arr[1]
    self.arr[1] = self.arr[self.n]
    self.n -= 1
    self.bubble_down(1)
    return minval

  """ Insert object val into the heap """
  def insert(self, val):
    if len(self.arr) == self.n+1:
      self.arr.append(val)
    else:
      self.arr[self.n] = val;
    self.n += 1
    self.bubble_up(self.n)
    return val

  """ Bubbles up the value at index i.
      Swap with your parent while you are less than it."""
  def bubble_up(self, i):
    while i/2 != 0 and self.arr[i] < self.arr[i/2]:
      self.arr[i/2], self.arr[i] = self.arr[i], self.arr[i/2]
      i = i/2

  """ Bubbles down the value at index i.
      Swap with your lowest child until you reach
      the bottom. Then stop. """
  def bubble_down(self, i):
    while 2*i <= self.n:
      if 2*i+1 > self.n or self.arr[2*i+1] > self.arr[i] or self.arr[2*i+1] > self.arr[2*i]:
        if self.arr[2*i] < self.arr[i]:
          self.arr[2*i], self.arr[i] = self.arr[i], self.arr[2*i]
          i = 2*i
        else:
          break
      elif self.arr[2*i+1] < self.arr[i]:
        self.arr[2*i+1], self.arr[i] = self.arr[i], self.arr[2*i+1]
        i = 2*i+1

  """ Heapifies the internal array """
  def heapify(self):
    for i in reversed(range(1,self.n+1)):
      self.bubble_down(i)

