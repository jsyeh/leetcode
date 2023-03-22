class Solution {
    public String countAndSay(int n) {
        if(n==1) return "1";
        String prev = countAndSay(n-1);

        String ans = "";
        char now=prev.charAt(0);
        int count=1;
        for(int i=1; i<prev.length(); i++){
            if(prev.charAt(i)==prev.charAt(i-1)){
                count++;
            }else{
                ans += count + "" + now;
                now = prev.charAt(i);
                count = 1;
            }
        }
        ans +=  count + "" + now;
        return ans;
    }
}
