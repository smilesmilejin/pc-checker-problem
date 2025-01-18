# DO NOT MODIFY THE NODE CLASS
class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# define helper function to check for the range this node must be in for the tree to be valid
def is_BST_helper(root, min_value, max_value):
    # if the root is empty, return True
    if not root:
        return True

    # check if the current value is in the acceptable range
    in_range = root.value > min_value and root.value < max_value
    if not in_range:
        return False

    # check the root's right side, updating the min value to be the current root's val
    right_check = is_BST_helper(root.right, root.value, max_value)
    # check the root's left side, updating the max value to be the current root's val
    left_check = is_BST_helper(root.left, min_value, root.value)

    return right_check and left_check


def is_BST(node):
    # return the results from calling the helper function with the root of the tree, and -infinity as the initial min value and infinity as the initial max value
    return is_BST_helper(node, float('-inf'), float('inf'))


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
