import heapq
class Solution:
	def findKthLargest(self, nums, k):
		heap = []
		for n in nums[:k]:
			heapq.heappush(heap, n)
		for n in nums[k:]:
			if n > heap[0]:
				heapq.heappop(heap)
				heapq.heappush(heap, n)
		return heap[0]


if __name__ == '__main__':
	s = Solution()
	nums = [3,2,1,5,6,4]
	k = 2
	result = s.findKthLargest(nums, k)
	print(result)