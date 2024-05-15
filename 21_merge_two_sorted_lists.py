def main():
    list1 = [1, 2, 4]
    list2 = [1, 3, 4]
    node_list_1 = list_to_node(list1)
    node_list_2 = list_to_node(list2)
    print("meow")


def merge_two_lists(node1, node2):
    if node1 != None and node2 != None:
        if node1.val > node2.val:
            node = ListNode()
            node.val = node2.val
            node.next = merge_two_lists(node1, node2.next)
        else:
            node = ListNode()
            node.val = node1.val
            node.next = merge_two_lists(node1.next, node2)
    elif not node1 and node2:
        node = ListNode()
        node.val = node2.val
        node.next = merge_two_lists(node1, node2.next)
    elif not node2 and node1:
        node = ListNode()
        node.val = node1.val
        node.next = merge_two_lists(node1.next, node2)

    elif node1 == None and node2 == None:
        None
    return node


def list_to_node(list_of_nums: list):
    if len(list_of_nums) == 1:
        node = ListNode()
        node.val = list_of_nums[0]
        node.next = None
    else:
        node = ListNode()
        node.val = list_of_nums[0]
        node.next = list_to_node(list_of_nums[1:])
    return node


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


if __name__ == "__main__":
    main()
