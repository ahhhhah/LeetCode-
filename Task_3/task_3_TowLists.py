# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
	def mergeTwoLists(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		# 增加头结点
		prehead = ListNode(-1)
		prev = prehead
		while l1 and l2:
			if l1.val < l2.val:
				prev.next = l1
				l1 = l1.next
			else:
				prev.next = l2
				l2 = l2.next
			prev = prev.next
		prev.next = l1 if l1 is not None else l2
		
		return prehead.next
		
if __name__ == '__main__':
	l1 = ListNode(1)
	l1.next = ListNode(2)
	l1.next.next = ListNode(4)
	
	l2 = ListNode(1)
	l2.next = ListNode(3)
	l2.next.next = ListNode(4)
	
	s = Solution()
	result = s.mergeTwoLists(l1, l2)
	
	print(result.val)