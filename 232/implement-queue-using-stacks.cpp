class MyQueue {
public:
    stack<int> q;
    stack<int> temp;
    MyQueue() {
        
    }
    
    void push(int x) {
        while(q.size()>0){
            temp.push(q.top());
            q.pop();
        }
        q.push(x);
        while(temp.size()>0){
            q.push(temp.top());
            temp.pop();
        }
    }
    
    int pop() {
        int temp = q.top();
        q.pop();
        return temp;
    }
    
    int peek() {
        return q.top();
    }
    
    bool empty() {
        return q.size()==0;
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */
