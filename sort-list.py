# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        slow = ListNode(0)
        slow.next = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        head1,head2 = head,slow.next
        slow.next = None
        tmp1,tmp2 = self.sortList(head1),self.sortList(head2)
        ans = ListNode(0)
        p = ans
        while tmp1 and tmp2:
            if tmp1.val < tmp2.val:
                p.next = tmp1
                tmp1,p = tmp1.next,p.next
            else:
                p.next = tmp2
                tmp2,p = tmp2.next,p.next
        if tmp1:
            p.next = tmp1
        if tmp2:
            p.next = tmp2
        return ans.next