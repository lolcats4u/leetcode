def main():
    list1 = [1, 2, 4]
    list2 = [1, 3, 4]
    node_list_1 = list_to_list_of_list_nodes(list1)
    node_list_2 = list_to_list_of_list_nodes(list2)
    print(mergeTwoLists(node_list_1, node_list_2))


def list_to_list_of_list_nodes(list_of_nums: list):
    list_of_list_nodes = []
    for index, num in enumerate(list_of_nums):
        try:
            node = ListNode()
            node.val = num
            node.next = list_to_list_of_list_nodes(list_of_nums[index:])
            return node
        except IndexError:
            node = ListNode()
            node.val = num
            node.next = None
            return node
    return list_of_list_nodes


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


if __name__ == "__main__":
    main()
