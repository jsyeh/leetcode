// LeetCode 2425. Bitwise XOR of All Pairings
// nums1 和 nums2 裡有「很多數」，左右排列組合配對 XOR 結果放在 nums3
// 問 nums3 裡「全部的數」XOR 的結果
class Solution {
public:
    int xorAllNums(vector<int>& nums1, vector<int>& nums2) {
        int M = nums1.size(), N = nums2.size(); // 左邊 M 個，右邊 N 個
        int ans = 0;
        // 其實，就看 XOR 幾次即可。XOR兩次，等於「沒有」XOR，所以只看「奇數」
        // 左邊、右邊配對，所以左邊的數，配對右邊 N 次
        if(N%2==1) { // 右邊是奇數時，左邊的數，才會「都算1次」
            for(int num : nums1) {
                ans ^= num;
            }
        }
        // 左邊、右邊配對，所以右邊的數，配對左邊 M 次
        if(M%2==1) { // 左邊是奇數時，右邊的數，才會「都算1次」
            for(int num : nums2) {
                ans ^= num;
            }
        }
        return ans;
    }
};
