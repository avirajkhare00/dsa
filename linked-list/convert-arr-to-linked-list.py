class Node:
  def __init__(self, data, head=None):
    self.data = data
    self.head = head


sample_arr = [1,2,3,4,5]

head = Node(sample_arr[0])
mover = head

for i in range(1, len(sample_arr)):
  temp = Node(sample_arr[i])
  head.head = temp
  mover = mover.head


print(head.data)
