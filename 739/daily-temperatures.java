class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int N = temperatures.length;

        Stack<Integer> stack = new Stack<Integer>();
        
        int[] ans = new int[N];
        for(int i=0; i<N; i++){
            int temp = temperatures[i];
            while(stack.size()>0 && temperatures[stack.peek()] < temp){
                //有待補/待更新的日子，且現在比之前熱，就回去補ans[prevDay]
                int prevDay = stack.pop();
                ans[prevDay] = i - prevDay;
System.out.println(prevDay + " " + i);
            }
            stack.push(i); //stack裡放著待補/待更新的ans[i]
        }

        return ans;
    }
}
