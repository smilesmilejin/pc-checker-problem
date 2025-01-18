# Checker Problem

Problem belonging to the post-classroom Mock Interview Question Repository.

## Problem Statement

We are interested in writing a function to check whether a tree is a binary search tree (BST).

For example:

```
           6
         /   \
        /     \
       3       8
      / \       \
     1   5       9
```

is a BST. For each node, all of the children in the left subtree are smaller, and all the children in the right subtree are larger.

However:

```
       5
      / \
     7   9
```

is NOT a BST because 7 is greater than 5.

Write a function that takes in the root of a tree and returns a boolean indicating whether the tree is a BST.

## Examples

### Additional Valid BST Examples

```
           6
         /   \
        /     \
       3       8
      / \       \
     1   5       9
```

```
       5
      / \
     3   9
```

```
           5
         /   \
        /     \
       3       7
      /         \
     1           8
    /             \
   0               9
```

### Additional Invalid BST Examples

```
       5
      / \
     7   9
```

```
       5
      / \
     3   4
```

```
           6
         /   \
        /     \
       3       8
      / \
     1   5
        /
       7
```
