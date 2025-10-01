// LeetCode 896. Monotonic Array
// 只有增加 or 只有減少 的陣列, 不可以「又有增、又有減」
class Solution {
public:
    bool isMonotonic(vector<int>& nums) {
        int up=0, down=0; // 如果有增加 up變成1 如果有減少 down變成1
        for(int i=1; i<nums.size(); i++) { // 陣列改從1開始
            if( nums[i-1] < nums[i] ) up = 1; // 左小、右大, 增加
            if( nums[i-1] > nums[i] ) down = 1; // 左大、右小, 減少
        }
        if(up==1 && down==1) return false; // 最後檢查, 不可以「又增加、又減少」
        return true;
    }
};
