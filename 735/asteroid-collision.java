class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        Stack<Integer> stack = new Stack<Integer>();
        for(int i=0; i<asteroids.length; i++) {
            int now = asteroids[i];
            if(now<0) {
                while(stack.size()>0 && stack.peek()>0) {
                    int prev = stack.pop();//可以行星互撞
                    if(-now==prev) {now = 0; break;} //一起都消失
                    if(-now>prev) continue;//繼續下一筆
                    if(-now<prev) {stack.push(prev); now=0; break;}
                }
                if(now!=0) stack.push(now);
            }else stack.push(now);
        }
        int[] ans = new int[stack.size()];
        for(int i=stack.size()-1; i>=0; i--){
            ans[i] = stack.pop();
        }
        return ans;
    }
}
