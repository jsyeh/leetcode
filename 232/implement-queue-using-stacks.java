class MyQueue {
    Stack<Integer> stack;
    Stack<Integer> temp;
    public MyQueue() {
        stack = new Stack<Integer>(); //real
        temp = new Stack<Integer>(); //temp
    }
    
    public void push(int x) {
        while(stack.size()>0){
            int now = stack.pop();
            temp.push(now);
        }
        stack.push(x);
        while(temp.size()>0){
            int now = temp.pop();
            stack.push(now);
        }
    }
    
    public int pop() {
        return stack.pop();
    }
    
    public int peek() {
        int now = stack.pop();
        stack.push(now);
        return now;
    }
    
    public boolean empty() {
        if(stack.size()==0) return true;
        else return false;
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */
