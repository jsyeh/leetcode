// LeetCode 1228. Missing Number In Arithmetic Progression
// 找到「等差級數」中，缺的那個數
class Solution {
public:
    int missingNumber(vector<int>& arr) {
        int diff = arr[1]-arr[0], diff2 = arr[2]-arr[1];
        if(diff<0) diff = max(diff,diff2);
        else diff = min(diff, diff2);

        if(diff==0) return arr[0];
        for(int i=0; i<arr.size()-1; i++){
            if(arr[i+1]-arr[i]!=diff) return arr[i]+diff;
        }
        return arr[0];
    }
};
