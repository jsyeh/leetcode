class Solution {
public:
    int myAtoi(string s) {
        int leading_space=0, sign=0;
        int N = s.length();
        for(int i=0; i<N; i++){
            if(s[i]==' ') leading_space++;
            else break;
        }
        if(s[leading_space]=='+') leading_space++;
        else if(s[leading_space]=='-') {leading_space++; sign=1; }
        long long int ans=0;
        for(int i=leading_space; i<N; i++){
            if(s[i]>='0' && s[i]<='9'){
                ans = ans * 10 + s[i]-'0';
            }else break;
            if(sign==1 && -ans<INT_MIN) return INT_MIN;
            if(sign==0 && ans>INT_MAX) return INT_MAX;
        }
        if(sign==1) return -ans;
        else return ans;
    }
};
