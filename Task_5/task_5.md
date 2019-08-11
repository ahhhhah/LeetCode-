# 78.子集

##### 难度 中等

# 题目描述

给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

**说明：解集不能包含重复的子集。**

## 示例

输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

## 解析

遍历数组,每次遇到一个数添加至一个新的集合中,并求该新集合的子集.


```Python
class Solution:
	def subsets(self, nums):
		res = [[]]
		for i in range(len(nums)):
			size = len(res)
			for j in range(size):
				tem = list(res[j])
				tem = tem.append(nums[i])
				res.append(tem)
		return res
```


## 传送门

来源：[力扣（LeetCode）](https://leetcode-cn.com/problems/subsets)
