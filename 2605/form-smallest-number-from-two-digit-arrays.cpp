// LeetCode 2605. Form Smallest Number From Two Digit Arrays
// nums1 和 nums2 「共有」的最小的數
// 或從 nums1 和 nums2 各挑1個數，組合出的2位數「要最小」
class Solution {
public:
    int minNumber(vector<int>& nums1, vector<int>& nums2) {
        int count[10] = {}; // 先統計數字出現次數
        for(int num : nums1) count[num]++;
        for(int num : nums2) count[num]++;
        for(int i=1; i<=9; i++) { // 從1到9巡，若出現2次，表示剛好都有，便是答案
            if(count[i]==2) return i;
        }
        // 若沒有共有的數，那就挑「最小的數」再組起來
        sort(nums1.begin(), nums1.end());
        sort(nums2.begin(), nums2.end());
        int d1 = nums1[0], d2 = nums2[0];
        return min(d1,d2)*10 + max(d1,d2);
    }
};
