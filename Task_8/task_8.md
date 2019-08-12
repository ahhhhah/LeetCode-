# 169.求众数

##### 难度 简单

## 题目描述

给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

**你可以假设数组是非空的，并且给定的数组总是存在众数。**

## 示例

输入: [3,2,3]
输出: 3

## 解析
```c++
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        return nums[nums.size()/2];
    }
};
```

## 传送门
[LeetCode](https://leetcode-cn.com/problems/majority-element/)