class Solution {
public:
    string addBinary(string a, string b) {
        int N1 = a.length(), N2 = b.length();
        if(a[0]=='0') return b;
        if(b[0]=='0') return a;
        
        char c[N1+N2+1];

        int i=N1-1, j=N2-1, k = N1+N2;
        int carry = 0;
        while(i>=0 && j>=0) {
            int now = a[i]-'0' + b[j]-'0' + carry;
            carry = now / 2;
            c[k] = now % 2 + '0';
            i--;
            j--;
            k--;
        }
        while(i>j) { //a[i]還有續命，繼續做
            int now = a[i]-'0' + carry;
            carry = now / 2;
            c[k] = now % 2 + '0';
            i--;
            k--;
        }
        while(j>i) { //b[j]還有續命，繼續做
            int now = b[j]-'0' + carry;
            carry = now / 2;
            c[k] = now % 2 + '0';
            j--;
            k--;
        }
        if(carry>0){
            c[k] = carry + '0';
            k--;
        }
        for(int i=k+1; i<N1+N2+1; i++){
            printf("%c ", c[i]);
        }
        //printf("k:%d, N1+N2+2-k:%d\n", k, N1+N2-k+1);
        //printf("N1:%d N2:%d\n", N1, N2);
        string ans(c+k+1, N1+N2+1-k-1);//string ans(c+k+1, N1+N2+2-k);
        return ans;
    }
};
