# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        head = ListNode(0)
        l3 = head
        flag = 0
        while l1 and l2:
            l3.next = ListNode((l1.val + l2.val + flag) % 10)
            flag = (l1.val + l2.val + flag) / 10
            l1 = l1.next
            l2 = l2.next
            l3 = l3.next
        if l2:
            while l2:
                l3.next = ListNode((l2.val + flag) % 10)
                flag = (l2.val + flag) / 10
                l3 = l3.next
                l2 = l2.next
        if l1:
            while l1:
                l3.next = ListNode((l1.val + flag) % 10)
                flag = (l1.val + flag) / 10
                l3 = l3.next
                l1 = l1.next
        if flag == 1:
            l3.next = ListNode(1)
        return head.next