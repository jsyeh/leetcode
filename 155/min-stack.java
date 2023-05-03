class MinStack {
    Stack<int[]> stack = new Stack<>();
    public MinStack() {
        
    }
    
    public void push(int val) {
        if(stack.size()>0) {
            int[] temp = {val, min(val, stack.peek()[1])};
            stack.push(temp);
        } else {
            int[] temp = {val, val};
            stack.push(temp);
        }
    }
    
    public void pop() {
        stack.pop();
    }
    
    public int top() {
        int [] temp = stack.peek();
        return temp[0];
    }
    
    public int getMin() {
        int [] temp = stack.peek();
        return temp[1];
    }

    int min(int a, int b) {
        if(a<b) return a;
        else return b;
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */
