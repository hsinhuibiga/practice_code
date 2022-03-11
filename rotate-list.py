class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
		if not head or k==0:
            return head
        
        size=0;
        tmp=ListNode(0)
        tmp.next=head
        cur=tmp
        while cur.next:
            size+=1
            cur=cur.next
        #此時cur指向最後一個結點，這裡先和head接上，變成一個環
        cur.next=head
        #找到新的頭結點的前一個結點，摘鏈
        for i in range(size-k%size):
            cur=cur.next
        #此時cur指向新的頭結點的前一個結點
        new_head=cur.next
        #摘鏈
        cur.next=None
        return new_head