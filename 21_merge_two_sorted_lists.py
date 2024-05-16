def main():
    list1 = [1, 2, 4]
    list2 = [1, 3, 4]
    list1 = list_to_node(list1)
    list2 = list_to_node(list2)
    node = mergeTwoLists(list1, list2)
    print(node)
    print("meow")


def mergeTwoLists(list1, list2):
    if list1 is not None and list2 is not None:
        if list1.val > list2.val:
            node = ListNode()
            node.val = list2.val
            node.next = mergeTwoLists(list1, list2.next)
        else:
            node = ListNode()
            node.val = list1.val
            node.next = mergeTwoLists(list1.next, list2)
    elif not list1 and list2:
        node = ListNode()
        node.val = list2.val
        node.next = mergeTwoLists(list1, list2.next)
    elif not list2 and list1:
        node = ListNode()
        node.val = list1.val
        node.next = mergeTwoLists(list1.next, list2)

    elif list1 is None and list2 is None:
        return None

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

    def __str__(self):
        return f"NodeObject(val: {self.val}, next: {self.next})"


if __name__ == "__main__":
    main()
