class Solution {
public:
    int reverse(int x) {
        int sign=0;
        if(x<-INT_MAX) return 0;
        if(x<0){
            sign = 1;
            x = -x;
        } 
        long long int ans=0;
        while(x>0){
            ans *=10;
            ans += x%10;
            if(ans>INT_MAX) return 0;
            x /=10;
            if(ans<0) return 0;
        }
        if(sign==1 && -ans<INT_MIN) return 0;
        if(sign==1) return -ans;
        return ans;
    }
};
