class Solution(object):
	def subsets(self, nums):
		res = [[]]
		for i in range(len(nums)-1, -1, -1):
			for subres in res[:]:
				res.append(subres+[nums[i]])
		return res
	
	def subsets2(self, nums):
		res=[[]]
		for i in range(len(nums)):
			size = len(res)
			for j in range(size):
				tmp = list(res[j])
				tmp.append(nums[i])
				res.append(tmp)
		return res
	
if __name__ == '__main__':
	
	def subsets2(nums):
		res=[[]]
		for i in range(len(nums)):
			size = len(res)
			for j in range(size):
				tmp = list(res[j])
				tmp.append(nums[i])
				res.append(tmp)
		return res
	
	nums = [1,2,3]
	s = Solution()
	print(subsets2(nums))
	