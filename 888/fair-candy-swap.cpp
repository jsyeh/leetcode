// LeetCode 888. Fair Candy Swap
// Alice 和 Box 有很多盒糖果，每盒糖果數量是 aliceSizes[i] bobSizes[j]
// 兩人想交換「一盒」糖果後，讓兩人糖果數量相同。換的是「幾個糖果」的盒子？
class Solution {
public:
    vector<int> fairCandySwap(vector<int>& aliceSizes, vector<int>& bobSizes) {
        int S1 = accumulate(aliceSizes.begin(), aliceSizes.end(), 0); // 兩人的糖果數
        int S2 = accumulate(bobSizes.begin(), bobSizes.end(), 0); // 兩人的糖果數
        int target = (S1-S2)/2; // Alice 要多給 Bob 的糖果數
        unordered_set<int> bob; // 把 Bob 每個盒子的糖果數，記入 set() 裡
        for(int b : bobSizes) bob.insert(b);

        for(int a : aliceSizes) { // 把 Alices 的每盒，逐一看看
            if( bob.count(a-target) > 0 ) { // 如果這盒 a 給 Bob，Bob 能回送 a-target 的盒子
                return vector<int> {a, a-target}; // 就找到答案了
            }
        }
        return vector<int>{0, 0}; // 題目保證這行不會走到，用來檢查return的
    }
};
