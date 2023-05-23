class Solution {
public:
    string multiply(string num1, string num2) {
        int N1 = num1.length(), N2 = num2.length();
        int a[N1+N2];
        for(int i=0; i<N1+N2; i++) a[i] = 0;

        for(int i=N1-1; i>=0; i--){
            for(int j=N2-1; j>=0; j--){
                int now = (num1[i]-'0') * (num2[j]-'0');
//printf("now:%d\n", now);
                a[i+j+1] += now;

                a[i+j] += a[i+j+1] / 10;
                a[i+j+1] = a[i+j+1] % 10;
            }
        }

        int leadingZero = 0;
        for(int i=0; i<N1+N2; i++){
            if(a[i]==0) leadingZero++;
            else break;
        }
//printf("leadingZero: %d\n", leadingZero);

        if(leadingZero==N1+N2) return "0";//全部都是0, 就例外處理

        char str[N1+N2-leadingZero];
        for(int i=leadingZero; i<N1+N2; i++) {
            str[i-leadingZero] = a[i]+'0';
        }
        string ans(str, N1+N2-leadingZero);
        return ans;
    }
};
//caes 2/311: "0" "0""
