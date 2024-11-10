// LeetCode 3097. Shortest Subarray With OR at Least K II
// 一堆數字「越 OR 越大」，因有「越來越多的1」。目標：用「連續的最少的數字」， OR 的結果，最少要是 k
// 數字太多了，可用「毛毛蟲」式的sliding window 來解，用 O(n) 完成
class Solution {
public:
    int findBits(int bits[32]) { // 從「累積的bits[i]裡，找出全部OR的結果
        int ans = 0;
        for(int i=0; i<32; i++){
            if(bits[i]>0) ans += (1<<i);
        }
        return ans;
    }
    int minimumSubarrayLength(vector<int>& nums, int k) {
        int bits[32] = {}; // 共有 32 個 bit，把每個bit看「累積」幾個「重覆的1
        int ans = INT_MAX; // 因要找「最小值」，預設值就先設「無限大」
        int left = 0; // 毛毛蟲的左邊
        for(int right = 0; right < nums.size(); right++) { // 毛毛蟲的右邊
            int numsRight = nums[right];
            for(int i=0; numsRight>0; i++, numsRight /= 2) {
                bits[i] += numsRight % 2; // 增加「對應的bit」
            }
            while(findBits(bits) >= k && left<=right) { // 合理，就「左邊縮短」
                ans = min(ans, right-left+1); // 並更新答案
                for(int i=0; nums[left]>0; i++, nums[left] /= 2){
                    bits[i] -= nums[left] % 2; // 減少「對應的bit」
                }
                left++;
            }
        }
        if(ans==INT_MAX) return -1; // 若是預設值「無限大」表示「沒找到答案」，回傳 -1
        return ans;
    }
};
