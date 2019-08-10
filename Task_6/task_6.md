# 148.排序链表

##### 难度:中等

## 题目描述

在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

## 示例

输入: 4->2->1->3
输出: 1->2->3->4

## 解析

要满足Ｏ(nlogn)的时间复杂度,常规手段有3种: 归并排序, 快速排序, 堆排序.
而同时满足常数级的空间复杂度,只能采用自顶向下的归并排序.


```c++
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* sortList(ListNode* head) {
        if (head == NULL || head->next == NULL) return head;
        ListNode *slow = head, *fast = head;
        while(fast->next != NULL && fast->next->next != NULL){
            slow = slow->next;
            fast = fast->next->next;
        }
        fast = slow->next;
        slow->next = NULL;
        ListNode *l1 = sortList(head);
        ListNode *l2 = sortList(fast);
        return mergeTwoLists(l1, l2);
    }

    ListNode *mergeTwoLists(ListNode *l1, ListNode *l2){
        ListNode dummy(-1); //创建头结点
        for(ListNode *p = &dummy; l1!=NULL || l2!=NULL; p=p->next){
            int val1 = l1==NULL?INT_MAX:l1->val;
            int val2 = l2==NULL?INT_MAX:l2->val;
            if(val1 <= val2){
                p->next = l1;
                l1 = l1->next;
            }
            else{
                p->next = l2;
                l2 = l2->next;
            }
        }
        return dummy.next;
    }
};
```

## 传送门
[LeetCode](https://leetcode-cn.com/problems/sort-list/)
