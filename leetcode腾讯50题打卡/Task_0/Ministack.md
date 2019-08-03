# 155.最小栈

## 问题描述

设计一个支持 push，pop，top 操作，并能在**常数时间内检索到最小元素**的栈。

push(x) -- 将元素 x 推入栈中。
pop() -- 删除栈顶的元素。
top() -- 获取栈顶元素。
getMin() -- 检索栈中的最小元素。

## 示例

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.

## 解析

常见数据结构栈的使用,因为题目要求**在常数时间内**检索到最小元素.
所以选择两个栈来实现MinStack

- 1. 存放给定的数据的data_stack,
- 2. 存放最小值的mini_stack,

输入结束后,mini_stack的栈顶元素即为栈中最小元素.

## 传送门
来源：[力扣（LeetCode）](https://leetcode-cn.com/problems/min-stack)
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

