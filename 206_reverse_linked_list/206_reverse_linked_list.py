from typing import *
def main(test):
    solution = Solution().reverseList()
    print(solution)

class Solution:
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    class LinkedList:
        def __init__(self, head: Optional[Solution.ListNode]=Solution.ListNode()):
            self.head = head 
            self.tail = self.traverse()

        def from_list(self, list):
            new_head = Solution.LinkedList(Solution.ListNode())

        def traverse(self):
            if not self.head:
                return None
            current_node = self.head
            while current_node:
                if current_node.next:
                    current_node = current_node.next
                else:
                    break
            return current_node
        
        def append(self, ListNode):
            ListNode.next = None
            if not self.head:
                self.head = ListNode
            else:
                self.tail.next = ListNode

        def prepend(self, ListNode):
            new_head = Solution.LinkedList(ListNode)
            if self.head:
                new_head.next = self.head
            else:
                new_head.next = None
            self.head = new_head

        def reverse(self):
            reversed_list = Solution.LinkedList()
            current_node = self.head
            while current_node:
                reversed_list.prepend(current_node)
                if current_node.next:
                    current_node = current_node.next
            self.reversed = reversed_list
            return self.reversed
        
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.LinkedList(head).reverse()

def tests():
    test_0 = [1,2,3,4,5]
    return locals().values()

if __name__ == "__main__":
    tests = tests()
    for test in tests:
        main(test)