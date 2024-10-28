// LeetCode 1893. Check if All the Integers in a Range Are Covered
// 測試 left...right 裡的整數，是否都有在 ranges 裡
class Solution {
public:
    bool isCovered(vector<vector<int>>& ranges, int left, int right) {
        int s[60] = {};
        for(auto range : ranges){
            for(int now=range[0]; now<=range[1]; now++){
                s[now]=1;
            }
        }
        for(int now=left; now<=right; now++){
            if(s[now]==0) return false;
        }
        return true;
    }
};
