class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = resList = ListNode(None)
        carry = 0
        while l1 or l2 :
            sum_val = carry
            if l1 != None:
                sum_val += l1.val
                l1 = l1.next
            if l2 != None:
                sum_val += l2.val
                l2 = l2.next
            carry = sum_val // 10
            resList.next = ListNode(sum_val % 10)
            resList = resList.next

        if carry == 1:
            resList.next = ListNode(carry)

        return dummy.next
           