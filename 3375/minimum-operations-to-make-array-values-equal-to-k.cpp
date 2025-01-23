// LeetCode 3375. Minimum Operations to Make Array Values Equal to K
// 每次可在 nums 挑個 valid 的數 h，比它大的數(都要相同)，都會變成 h
// 要讓 nums 裡全部的數都變成 k，最少要幾步？
// 問題等價成：如果把數字「小到大」排好，有幾個「不同」的數？要退幾步，才會變成k
class Solution {
public:
    int minOperations(vector<int>& nums, int k) {
        unordered_set<int> diff; // 有幾個不同的數
        for(int num : nums) {
            diff.insert(num);
            if(num<k) return -1; // 如果有數比 k 小，那一定無法達成任務
        }
        diff.insert(k);
        return diff.size() - 1;
    } // 總共有 len(diff)不同的數，要退到最小的k，要再-1步
};
