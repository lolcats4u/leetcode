def main():
    list1 = [1, 2, 4]
    list2 = [1, 3, 4]
    node_list_1 = list_to_node(list1)
    node_list_2 = list_to_node(list2)


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
