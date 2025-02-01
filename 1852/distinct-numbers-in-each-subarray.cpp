// LeetCode 1852. Distinct Numbers in Each Subarray
// 在 nums 裡，連續 k 個數裡，會有幾個「不同」的數？
// 答案是陣列，因「連續 k 個數」左到右滑動，會有 n-k+1 種可能
class Solution {
public:
    vector<int> distinctNumbers(vector<int>& nums, int k) {
        // 使用 hash map 對應出「某數的頻率」
        unordered_map<int,int> freq;
        for(int i=0; i<k; i++) freq[nums[i]]++; // 先將前k 項準備好
        vector<int> ans(nums.size()-k+1);
        ans[0] = freq.size();
        for(int i=0; i<nums.size()-k; i++) { // 口訣： +k -k 對消
            freq[nums[i+k]]++;
            freq[nums[i]]--;
            if(freq[nums[i]]==0) freq.erase(nums[i]);
            ans[i+1] = freq.size();
        }
        return ans;
    }
};
