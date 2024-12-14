// LeetCode 2762. Continuous Subarrays
// 數字很接近的 subarray，長度可能不同，但「裡面每一項」數字距離<=2
// 問這樣的subarray有幾個？可用毛毛蟲 左邊尾巴j 右邊頭i 持續更新「還能容忍的上下界」直到失敗重來
class Solution {
public:
    long long continuousSubarrays(vector<int>& nums) {
        long long ans = 1; // 全部累計「有幾種」這樣的 subarray
        int up = nums[0] + 2, down = nums[0] - 2; // 一開始數字的上下邊界
        int j = 0; // 毛毛蟲的左邊尾巴
        for (int i=1; i<nums.size(); i++) { // 毛毛蟲的右邊頭
            if(down <= nums[i] && nums[i] <= up) { // 還在範圍內，持續加長
                up = min(up, nums[i]+2); // nums[i] 可能拉低上界
                down = max(down, nums[i]-2); // nums[i] 可能抬高下界
                ans += i-j+1; // 現在 subarray 又多這麼多可能，右邊頭都在i
            } else { // 不幸超過界限範圍，尾巴j 要重新找到
                j = i; // 左邊尾巴j 
                up = nums[i] + 2; // 從右邊頭為主，將往左檢查、更新「上界」
                down = nums[i] - 2; // 從右邊頭為主，將往左檢查、更新「下界」
                while(down <= nums[j-1] && nums[j-1] <= up) { // 若左邊 nums[j-1] 在界限內
                    j--; // 可左移，剛剛 nums[j-1] 現在改叫 nums[j] 項了
                    up = min(up, nums[j] + 2); // 加入 nums[j] 後可能限縮上界
                    down = max(down, nums[j] - 2); // 可能限縮下界
                }
                ans += i-j+1; // 現在 subarray 又多這麼多可能，右邊頭都在i
            }
        }
        return ans;
    }
};
