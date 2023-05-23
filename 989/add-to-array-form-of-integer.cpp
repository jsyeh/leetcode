class Solution {
public:
    vector<int> addToArrayForm(vector<int>& num, int b) {
        
        int a[10004]; //int a[5];
        vector<int> num2;
        for(int i=4; i>=0; i--) {
            a[i] = b%10;
            b = b / 10;
            if(b==0) { //最高位數也存好了
                for(int z=i; z<5; z++){
                    num2.push_back(a[z]);
                }
                break;
            }
        }
        int i = num.size() - 1, j = num2.size() - 1, k = 0, carry = 0;
        while( i>=0 && j>=0 ) {
            a[k] = num[i] + num2[j] + carry;
            carry = a[k] / 10;
            a[k] = a[k] % 10;
            i--;
            j--;
            k++; //a[k] 是從底位到高位存, 之後再反回來做
        }
        if(i>j){
            while(i>=0) {
                a[k] = num[i] + carry;
                carry = a[k] / 10;
                a[k] = a[k] % 10;
                i--;
                k++;
            }
        }
        if(j>i){
            while(j>=0) {
                a[k] = num2[j] + carry;
                carry = a[k] / 10;
                a[k] = a[k] % 10;
                j--;
                k++;
            }
        }
        if(carry>0){
            a[k] = carry;
            k++;
        }
        vector<int> ans(k);
        for(int i=0; i<k; i++){
            ans[i] = a[k-1-i];
        }

        return ans;
    }
};
