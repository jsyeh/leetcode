class Solution {
    public int findTheLongestBalancedSubstring(String s) {
        int N = s.length();
        int ans = 0;
        int zero=0, one=0;
        int state=0; //0: finding zero, 1: finding one
        int next=0;
        for(int k=next; k<N; k++) {
            if(state==0 && s.charAt(k)=='0') {
                zero++;
            }else if(state==0 && s.charAt(k)=='1') {
                state=1;
                one++;
            }else if(state==1 && s.charAt(k)=='0') {
                //find answer
                int now = (zero<one)? zero:one;
                if(now*2>ans) ans = now*2;
                one=0;
                zero=1;
                state=0;
                next = k; //這裡要想一下
            }else if(state==1 && s.charAt(k)=='1') {
                one++;
            }
        }
        System.out.println(zero + " " + one);
        if(state==1){
            //find answer
            int now = (zero<one)? zero:one;
            if(now*2>ans) ans = now*2;
            one=0;
            zero=0;
            state=0;
        }
        return ans;
    }
}
