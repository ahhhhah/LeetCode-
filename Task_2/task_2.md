# 215. 数组中的第K个最大元素

## 问题描述
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

## 示例
输入: [3,2,1,5,6,4] 和 k = 2
输出: 5

## 解析
**思路参考LeetCode题解评论区**

1. 构造小顶堆,
2. 将数组中前k个元素添加到堆中,
3. 数组中后n-k个元素中若存在比堆顶元素大的值,则将其添加至堆中(此时的堆重新排列),
4. 保持堆中元素个数为k,
5. 遍历结束后,堆顶元素即为所求.

#### 其他思路
- 还可以将数组元素排序后,根据大小顺序取第k个元素.
- 快速选择排序(没看)
#### 什么是堆?
**堆是一个完全二叉树(或满二叉树)**
大顶堆: 堆顶元素比其他节点元素都大,
小顶堆: 堆顶元素比其他节点元素都小.

#### 怎样创建堆?
```c++
#include<iostream>
#include<algorithm>
#include<vector>

vector<int> nums;
// 小顶堆
meak_heap(nums.begin(), nums.end(), greater<int>());

// 大顶堆
meak_heap(nums.begin(), nums.end(),);
```

```python
import heapq

list = []
for num in nums:
	heapq.heappush(heap, n)
```

## 传送门
[c++堆](http://c.biancheng.net/view/481.html)
[python堆](http://c.biancheng.net/view/2432.html)
[leetcode](https://leetcode-cn.com/problems/kth-largest-element-in-an-array/)

