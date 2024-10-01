# Given a singly linked list, reverse the order of its nodes.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create nodes
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

# write a function to reverse it

def reverse_linked_list(head):
  elements = []
  while hasattr(head, 'next'):
    elements.append(head.data)
    head = head.next
  reversed_elements = list(reversed(elements))
  new_head = Node(None)
  for i in reversed_elements:
    new_head.data = i
    new_head.next = Node(None)

reverse_linked_list(head)
