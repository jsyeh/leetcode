// LeetCode 3011. Find if Array Can Be Sorted
// 使用經典的 Bubble Sort 泡泡排序法，模擬題目的運程：相鄰的（且bits裡1的數目相同）可交換。
class Solution {
public:
    bool canSortArray(vector<int>& nums) {
        int N = nums.size();
        vector<int>bits(N);
        for(int i=0; i<N; i++){ // 先統計 nums[i] 的 bits數
            for(int b=0; b<32; b++) {
                if(nums[i]&(1<<b)) bits[i]++;
            }
        }
        bool swapped = true;
        while(swapped) {
            swapped = false;
            for(int i=0; i<N-1; i++) {
                if(nums[i]>nums[i+1]){
                    if(bits[i]!=bits[i+1]) return false;
                    int temp = nums[i];
                    nums[i] = nums[i+1];
                    nums[i+1] = temp;
                    temp = bits[i];
                    bits[i] = bits[i+1];
                    bits[i+1] = temp;
                    swapped = true;
                }
            }
        }
        return true;

    }
};
