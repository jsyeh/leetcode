class Solution {
    public boolean validateStackSequences(int[] pushed, int[] popped) {
        //simulation開始
        Stack<Integer> stack = new Stack<Integer>();
        int k = 0; //k for popped[k]
        for(int i=0; i<pushed.length; i++){
            stack.push(pushed[i]);
            while(stack.size()>0 && k<popped.length && stack.peek()==popped[k]){
                stack.pop();
                k++;
            }
        }
        if(stack.size()==0) return true;
        else return false;
    }
}//case 3: [1,0] [1,0]
