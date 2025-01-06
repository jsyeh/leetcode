// LeetCode 1217. Minimum Cost to Move Chips to The Same Position
// 移動「偶數步」不用cost，移動1步要cost=1，把全部 chips 籌碼移到同一格，要多少 cost?
class Solution {
public:
    int minCostToMoveChips(vector<int>& position) {
        // 因為移動「偶數步」不用cost，所以所有的偶數可放一堆、奇數也能放一堆
        int odd = 0, even = 0; // 分成「奇數堆、偶數堆」
        for(int p : position) {
            if(p%2==0) even++;
            else odd++;
        }
        //  比較小堆的，是答案，因為它們要移到「另一堆」大堆的。
        return min(odd, even);
    }
};
