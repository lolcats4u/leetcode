from typing import Optional

def main(test_head_node):
    solution = Solution()
    copy = solution.copyRandomList(test_head_node)
    print(copy)


class Node:
    def __init__(self, x: int, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class LinkedList:
    def __init__(self):
        self.head_node = None

    def append(self, node: Optional[Node]):
        if not self.head_node:
            self.head_node = node
            return
        head = self.head_node
        while head.next:
            head = head.next
        head.next = node

class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        new_list = LinkedList()
        current = head
        while current:
            new_list.append(Node(int(), int(), None))
        return new_list

def tests():
    test = [[7,None],[13,0],[11,4],[10,2],[1,0]]
    return locals()

if __name__ == "__main__":
    for _, test in tests().items():
        main(test)
