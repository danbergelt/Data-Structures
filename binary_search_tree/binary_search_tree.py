import sys
sys.path.append('../queue_and_stack')
from dll_stack import Stack
from dll_queue import Queue


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
      # If inserting we must already have a tree/root
      # If value is < root go left, make a new tree/node if empty, otherwise keep going(recursion)
      # If greater than or equal to then go right, make a new tree/node if empty, otherwise keep going(recursion)
        if self.value == None:
            self.value = value
            return self.value
        elif value < self.value:
            if self.left == None:
                self.left = BinarySearchTree(value)
            else:
                return self.left.insert(value)
        else:
            if self.right == None:
                self.right = BinarySearchTree(value)
            else:
                return self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
      # If target == self.value, return it
      # go left or right based on smaller or bigger
        if self.value == target:
            return self.value
        elif target < self.value:
            if self.left == target:
                return self.left
            elif self.left == None:
                return None
            else:
                return self.left.contains(target)
        else:
            if self.right == target:
                return self.right
            elif self.right == None:
                return None
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
      # if right exists, go right
      # otherwise return self.value
        if self.right != None:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        if self.value == None:
            return None
        else:
            cb(self.value)
            if self.right != None:
                self.right.for_each(cb)
            if self.left != None:
                self.left.for_each(cb)
        return

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        if node:
            self.in_order_print(node.left)
            print(node.value)
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self, node):
      # make a queue
      # put root in queue
      # while queue not empty
      #     pop root out of queue
      #     DO THE THING HERE
      #     if left
      #       add left to queue
      #     if right
      #       add right to queue
        queue = Queue()
        queue.enqueue(node)
        while queue.len() > 0:
            popped = queue.dequeue()
            print(popped.value)
            if popped.left:
                queue.enqueue(popped.left)
            if popped.right:
                queue.enqueue(popped.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
      # make a stack
      # put root in stack
      # while stack not empty
      #    pop root ouf ot stack
      #    DO THE THING HERE
      #    if left
      #        add left to stack
      #    if right
      #        add right to stack
      #
        stack = Stack()
        stack.push(node)
        while stack.len() > 0:
            popped = stack.pop()
            print(popped.value)
            if popped.left:
                stack.push(popped.left)
            if popped.right:
                stack.push(popped.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

# bst = BinarySearchTree(1)
# bst.insert(8)
# bst.insert(5)
# bst.insert(7)
# bst.insert(6)
# bst.insert(3)
# bst.insert(4)
# bst.insert(2)

# bst.bft_print(bst)
