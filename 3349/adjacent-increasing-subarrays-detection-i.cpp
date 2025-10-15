// LeetCode 3349. Adjacent Increasing Subarrays Detection I
// nums 陣列裡, 數字有些會增加。請問有沒有2個相鄰陣列, 裡面都是增加?
// ex.  2,5,7,8,9,2,3,4,3,1
//combo 1 2 3 4 5 1 沒有比較大,就不會再增加, 用原來的值1
class Solution {
public:
    bool hasIncreasingSubarrays(vector<int>& nums, int k) {
        // 使用玩遊戲常見的 combo 連續
        int N = nums.size(); // 陣列大小
        vector<int> combo(N, 1); //有N格,裡面都放 原來的值1
        for(int i=1; i<N; i++) {
            if( nums[i-1] < nums[i] ) combo[i] = combo[i-1] + 1;
        } // 變出 combo 陣列裡面全部的值, 有合格,就比前一項+1
        // 要檢查「相鄰2個長度為k的陣列, combo值夠不夠 k個連續
        for(int i=0; i<N-k; i++) {
            if( combo[i]>=k && combo[i+k]>=k ) return true;
        }
        return false;
    }
};
