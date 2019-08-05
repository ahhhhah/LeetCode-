#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution{
    public:
        int findKthLargest(vector<int>& nums, int k){
            vector<int> minstack(k);
            for(int i = 0; i < k; i++){
                minstack[i] = nums[i];
            }
            // 创建小顶堆
            make_heap(minstack.begin(), minstack.end(), greater<int>()); 
            for(int i = k; i < nums.size(); i++){
                // 如果比根节点大 插入堆中
                if(nums[i] > minstack[0]){
                    minstack.push_back(nums[i]);
                    push_heap(minstack.begin(), minstack.end(), greater<int>());
                }
                // 保持堆的大小为k
                if(minstack.size() > k){
                    pop_heap(minstack.begin(), minstack.end(), greater<int>());
                    minstack.pop_back();
                }
            }
            // 堆顶元素即为第k个最大的元素
            return minstack[0];
        }
};

