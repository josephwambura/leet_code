"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root

        def populate(node, right):
            node.next = right
            if node.left:
                populate(node.left, node.right)

                if right:
                    populate(node.right, right.left)
                else:
                    populate(node.right, None)

        populate(root, None)

        return root
