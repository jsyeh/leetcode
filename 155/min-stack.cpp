class MinStack {
public:
    stack<vector<int>> s;
    MinStack() {
        
    }
    
    void push(int val) {
        vector<int> temp;
        temp.push_back(val);
        temp.push_back(val);
        if(s.size()>0) temp[1] = min(val, s.top()[1]);
        s.push(temp);
    }
    
    void pop() {
        s.pop();
    }
    
    int top() {
        return s.top()[0];
    }
    
    int getMin() {
        return s.top()[1];
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
