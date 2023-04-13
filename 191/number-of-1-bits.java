public class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        int ans=0;
        if(n<0){
            if((n&0x80000000)!=0){
                ans++;
                n = n ^ 0x80000000;
            }
        }
        while(n!=0){
            if(n%2==1) ans++;
            n /= 2;
        }
        return ans;
    }
}//遇到負數時，另外處理，因n%2==-1
//case 4: 10000000000000000000000000000000
//case 5: 10101010101010101010101010101010
