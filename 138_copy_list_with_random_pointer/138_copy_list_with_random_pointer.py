from typing import Optional


def main(test):
    print(LinkedList(test))



def tests():
    test_1 = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
    test_2 = [[1, 1], [2, 1]]
    test_3 = [[3, None], [3, 0], [3, None]]
    return locals().values()


class Node:
    def __init__(self, x: int, next: "Node" = None, random: Node = None):
        self.val = int(x)
        self.next = next
        self.random = random


class LinkedList:
    def __init__(self, test_list):
        self.head:Node = self.transform_list(test_list)
        self.copy:Node = self.copyRandomList(self.head)

    def transform_list(self, test_list: list):
        for i in range(len(test_list)):
            if len(test_list) > 1:
                node = Node(test_list[i][0])
                node.random = test_list[i][1]
                node.next = self.transform_list(test_list[(i + 1) :])
            else:
                node = Node(test_list[i][0])
                node.random = test_list[i][1]
            return node

    def append(self, node: Node):
        not_last = None
        while self.head.next:
            not_last = self.head.next
        not_last.next.next = node

    def __str__(self):
        nodes = [self.head, self.copy]
        str_list = []
        for node in nodes:
            print_str = ""
            while node.next:
                print_str += f"val= {node.val}, next = {node.next}, random = {node.random} \n"
                
            print_str += f"val= {node.val}, next = {None},  random = {node.random} \n"
            str_list.append(print_str)


        total_print_str = f"""
Original List: 
{str_list[0]}\n

________________________________________

Copied List:
{str_list[1]}\n
                            """
        return total_print_str

    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        current_node = None
        new_next = None
        while head.next:
            current_node = Node(head.val, head.next, head.random)
            head = head.next
            new_next = Node(head.val, head.next, head.random)
            current_node.next = new_next
        return Node(head.val, None, head.random) 

if __name__ == "__main__":
    tests = tests()
    for test in tests:
        main(test)
