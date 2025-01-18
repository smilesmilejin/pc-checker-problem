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

## Notes for the Interviewer

#### Q: What should I do if two nodes have equal values?

A: You can assume each node will have a different value.

#### Q: What should I do if the input is None or has fewer than two nodes?

A: You can assume the tree will include at least one Node.

#### Q: Will the input contain any cycles?

A: No.

#### Q: What should I do if invalid input is passed in?

A: You can assume that the input will be valid.

#### Q: What data types will be stored in the values?

A: Integers, but more generally, if we assume that all the values in the list are mutually comparable, would the type matter?

### Hints

- If your candidate struggles with an initial algorithm, encourage them to walk through an example and describe how they would do it using only pen and paper.

- If your candidate still struggles, ask them to think through the simpler case where there's only 3 nodes (the 5, 7, and 9 example in the prompt). Ask them how they would walk through that one.

- If your candidate struggles to pass the last test in the suite, ask them to consider the use case of when one of the root's grandchildren has an invalid value. What can we do to ensure nodes further down in the tree are in an acceptable range?

- It can be challenging to debug this problem. If your candidate is failing a test and unsure why, encourage them to add print statements that help them see what nodes are being visited when. This can especially help if their code gets stuck in an infinite loop.

## Optional Bonus At-Home Challenges

To be attempted after completing the interview.

- What are the time/space complexities of the sample solution? Does it make a difference whether the tree is balanced or not?

- What type of traversal does the sample solution perform over the tree?

- If you wrote a recursive solution, try writing an iterative one. If you wrote an iterative solution, try writing a recursive one. Which do you prefer? What are the tradeoffs?

- Try extending your function to allow for Nodes with duplicate values.

- Try extending your function to use a custom comparator. It should accept an additional argument, `key`, that determines the order the BST ought to be using. For example, instead of checking which number is bigger, it could check which string is longer.
