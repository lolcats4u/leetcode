
class Solution:
    def __init__(self):
        self.nodelist = []
    def addTwoNumbers(self, l1, l2):
        if l2 and l1:
            sum = l1.val + l2.val
            if l1.carry or l2.carry:
                sum +=1
            if sum > 9:
                carry = True
            if carry:
                l1.carry = True
                l2.carry = True
            if l1.next and not l2.next:
                self.addTwoNumbers(l1.next, None)
            elif not l1.next and l2.next:
                self.addTwoNumbers(None,l2.next)
            elif l1.next and l2.next:
                self.addTwoNumbers(l1.next,l2.next)
            else:
                if carry:
                    return ListNode(1,self.addTwoNumbers(l1, l2))
                else:
                    return ListNode(sum,self.addTwoNumbers(l1.next, l2.next))
        elif not l1:
            if l2.next:
                sum = l2.val
                if l2.carry:
                    sum +=1
                if sum > 9:
                    l2.carry = True
                self.addTwoNumbers(None, l2.next)
            else:
                if l2.carry:
                    l2.carry = False
                    return ListNode(1,self.addTwoNumbers(None,l2))
        else:
            if carry:
                l1.carry = True
            self.addTwoNumbers(l1, None)


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

