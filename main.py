# DO NOT MODIFY THE NODE CLASS
class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def is_BST(node):
    # Your solution here!
    pass

    # check if left node is smaller than root
      # if not
        # return false
    # check if right node is smaller than root
      # if not
        # return false

  # return true



  # current node starts with BST root

  # queue
  # add the current node to the queue

  # while queue is not empty:
    # add left node to queue
    # add right node to queue
    # current pop the first element from queue

    # if left > current:
      # return false

    # if right < current:
      # return false

  # return True

    from collections import deque
    queue = deque()
    queue.append(node)

    # print('queue: ', queue)
    # print('queue value: ', queue[0].value)

    # current = node

    while queue:
      current_node = queue.popleft()

      # print('current_node value: ', current_node.value)

      if current_node.left and current_node.left.value > current_node.value:
          return False     
      if current_node.right and current_node.right.value < current_node.value:
          return False
      
      if current_node.left:
        queue.append(current_node.left)
      if current_node.right:
          queue.append(current_node.right)


    return True


r'''
           6
         /   \
        /     \
       3       8
      / \       \
     1   5       9

Valid: True
'''
tree = Node(6, Node(3, Node(1), Node(5)), Node(8, None, Node(9)))
assert is_BST(tree) == True

r'''
       5
      / \
     7   9

Valid: False
'''
tree = Node(5, Node(7), Node(9))
assert is_BST(tree) == False

r'''
       5
      / \
     3   9

Valid: True
'''
tree = Node(5, Node(3), Node(9))
assert is_BST(tree) == True

r'''
       5
      / \
     3   4

Valid: False
'''
tree = Node(5, Node(3), Node(4))
assert is_BST(tree) == False

r'''
           6
         /   \
        /     \
       3       8
      / \
     1   5
        /
       7

Valid: False
'''
tree = Node(6, Node(3, Node(1), Node(5, Node(7))), Node(8))
assert is_BST(tree) == False

r'''
           5
         /   \
        /     \
       3       7
      /         \
     1           8
    /             \
   0               9

Valid: True
'''
tree = Node(5, Node(3, Node(1, Node(0))), Node(7, None, Node(8, None, Node(9))))
assert is_BST(tree) == True

print("All tests passed!")
print("Discuss time & space complexity if time remains.")
