// LeetCode 1796. Second Largest Digit in a String
// 把字串 s 裡的數字取出來，問「第2大」的數字是誰。
class Solution {
public:
    int secondHighest(string s) {
        int counter[10] = {};
        for(char c : s) {
            if(isdigit(c)) {
                counter[c-'0']++; 
            }
        }
        int largest = 0;
        for(int i=9; i>=0; i--) {
            if(counter[i]>0) largest++;
            if(largest==2) return i;
        }
        return -1;
    }
};
