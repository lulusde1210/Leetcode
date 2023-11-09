"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodeToCopy = {None:None}

        curr = head
        while curr:
            newNode = Node(curr.val)
            nodeToCopy[curr] = newNode
            curr = curr.next
        
        iter = head
        while iter:
            copy = nodeToCopy[iter]
            copy.next = nodeToCopy[iter.next]
            copy.random = nodeToCopy[iter.random]
            iter = iter.next
        
        return nodeToCopy[head]
        