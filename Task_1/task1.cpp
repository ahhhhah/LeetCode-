#include <iostream>
#include <stack>
#include <string>

using namespace std;

class Solution{
public:
    stack<char> left_stack;
    // stack<char> right_stack;
    bool isValid(string s){
        left_stack.push('#');       // 增加开始字符
        for(int i = 0; i < s.length(); i++){
            if (s[i] == '(' || s[i] == '{' || s[i] == '['){
                left_stack.push(s[i]);
            }
            else if (s[i] == ')' && left_stack.top() == '('){
                left_stack.pop();
            }
            else if( s[i] == '}' && left_stack.top() == '{'){
                left_stack.pop();
            }
            else if( s[i] == ']' && left_stack.top() == '['){
                left_stack.pop();
            }
        }

        if (left_stack.top() == '#' && s.length()%2==0) return true;
        else return false;
    }
};


int main(){
    string s;
    cin >> s;
    cout<<s.length()<<endl;
    Solution soul;
    if (soul.isValid(s))    cout<<"true"<<endl;
    return 0;
}