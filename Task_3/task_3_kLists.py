# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
	# 暴力法
	def mergeKLists(self, lists):
		"""
		:type lists: List[ListNode]
		:rtype: ListNode
		"""
		head = point = ListNode(0)
		reslut = []
		for i in lists:
			while i:
				reslut.append(i.val)
				i = i.next
		reslut.sort()
		for x in reslut:
			# 新建一个节点
			point.next = ListNode(x)
			point = point.next
		return head.next


if __name__ == '__main__':
	l1 = ListNode(1)
	l1.next = ListNode(2)
	l1.next.next = ListNode(4)
	
	l2 = ListNode(1)
	l2.next = ListNode(3)
	l2.next.next = ListNode(4)
	
	l = [l1,l2]
	s = Solution()
	result = s.mergeKLists(l)
	
	print(result.val)