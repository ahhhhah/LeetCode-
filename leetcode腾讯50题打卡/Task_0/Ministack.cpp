#include<iostream>
#include<stack>

using namespace std;

class MinStack{
    public:
        stack<int> data_stack;
        stack<int> mini_stack;
        
        void push(int x){
            data_stack.push(x);
            if (mini_stack.empty()){
                mini_stack.push(x);
            }
            else if (mini_stack.top() >= x) {
                mini_stack.push(x);
            }
        }
    
        void pop(){
            if(mini_stack.top() == data_stack.top()){
                mini_stack.pop();
            }
            data_stack.pop();
        }
    
        int top(){
            return data_stack.top();
        }
    
        int getMin(){
            return mini_stack.top();        
        }
};

