# 136.只出现一次的数字

##### 难度 简单

## 题目描述

给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。
找出那个只出现了一次的元素。

**说明  你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？**

## 示例

输入: [2,2,1]
输出: 1

输入: [4,1,2,1,2]
输出: 4

## 解析

### 方法一

由于数组中仅有一个元素出现一次,其余的都出现两次.则只出现一次的元素为:
$$
a~x~=2\times\sum a~i~ - \sum a~i~
$$

```c++
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        //if(nums.empty() || nums.size() == 1)  return nums;
        int sum = accumulate(nums.begin(), nums.end(),0);
        sort(nums.begin(), nums.end());
        nums.erase(unique(nums.begin(), nums.end()), nums.end());
        int temp = 2*accumulate(nums.begin(), nums.end(), 0)-sum;
        return temp;
    }
};
```

### 方法二  位运算

- 任何数与0异或都不改变它的值, 即a $\bigoplus$ 0 = a
- 任何数与其自身异或都为0, 即a $\bigoplus$ a =0

因此,我们可以遍历整个数组.对每个元素进行异或处理后,得到的数即为整个数组中只出现一次的数字.

```python
class Solution:
	def singNumber(self, nums):
		ret = 0
		for num in nums:
			ret^=num
		return ret
```


## 传送门
[LeetCode](https://leetcode-cn.com/problems/single-number/)

