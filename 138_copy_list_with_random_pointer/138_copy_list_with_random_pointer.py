from typing import Optional
def main(test):
    solution = Solution().copyRandomList(LinkedList(test))

def tests():
    test_1 = [[7,None],[13,0],[11,4],[10,2],[1,0]]
    return locals().values()

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
class LinkedList:
    def __init__(self, test_list):
        self.head = self.transform_list(test_list)
    def transform_list(self, test_list:list):
        for i in range(len(test_list) -1):
            node = Node(test_list[i][0])
            node.random = test_list[i][1]
            node.next = self.transform_list(test_list[1:])
            return node.next

class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        pass


if __name__ == "__main__":
    tests = tests()
    for test in tests:
        main(test)