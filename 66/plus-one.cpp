class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int carry = 0;
        digits[digits.size()-1]++;
        for(int i=digits.size()-1; i>=0; i--) {
            digits[i] += carry;
            carry = digits[i] / 10;
            digits[i] = digits[i] % 10;
        }
        if(carry==0) return digits;
        else{
            vector<int> ans(digits.size()+1);
            ans[0] = 1;
            for(int i=0; i<digits.size(); i++){
                ans[i+1] = digits[i];
            }
            return ans;
        }
    }
};
