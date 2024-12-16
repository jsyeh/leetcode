// LeetCode 2011. Final Value of Variable After Performing Operations
// "++X", "X++", "--X", "X--" 共四種操作，X 開始是 0 問最後結束時 X 的值
class Solution {
public:
    int finalValueAfterOperations(vector<string>& operations) {
        int x = 0;
        for (string op : operations) {
            if(op[1]=='+') x++;
            else x--;
        }
        return x;
    }
};
