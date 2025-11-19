// LeetCode 2154. Keep Multiplying Found Values by Two
// 聰明的方法, 用到沒教過的 HashMap or HashSet
class Solution {
public:
    int findFinalValue(vector<int>& nums, int original) {
        set<int> numsSet; // HashSet 可以快速找到「有沒有這個數」
        for (int num : nums) numsSet.insert(num); // C++的進階迴圈
        // 請問 original 有沒有在 numsSet 裡? 有的話, 繼續一直做
        while ( numsSet.find(original) != numsSet.end() ) { // 沒有「沒有找到」
            original = original * 2;
        }
        return original;
    }
};
