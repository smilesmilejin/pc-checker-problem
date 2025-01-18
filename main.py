# DO NOT MODIFY THE NODE CLASS
class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def is_BST(node):
    # Your solution here!
    pass


'''
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

'''
       5
      / \
     7   9

Valid: False
'''
tree = Node(5, Node(7), Node(9))
assert is_BST(tree) == False

'''
       5
      / \
     3   9

Valid: True
'''
tree = Node(5, Node(3), Node(9))
assert is_BST(tree) == True

'''
       5
      / \
     3   4

Valid: False
'''
tree = Node(5, Node(3), Node(4))
assert is_BST(tree) == False

'''
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

'''
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
