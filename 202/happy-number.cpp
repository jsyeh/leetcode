class Solution {
public:
    int next(int n) {
        int ans=0;
        while(n>0){
            ans += (n%10)*(n%10);
            n = n / 10;
        }
        return ans;
    }
    bool isHappy(int n) {
        int n2 = n;
        while(n!=1) {
            n = next(n);
            n2 = next(next(n2));
            if(n==n2 && n!=1) return false;
        }
        return true;
    }
};
