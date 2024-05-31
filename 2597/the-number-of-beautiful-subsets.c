// LeetCode 2597. The Number of Beautiful Subsets
// 題目給個k，希望找到的 subset 裡各數的距離，不能 == k
// 所以有數字出現時， +k -k 的兩數都要避掉
// subset 的問題，不能用暴力法去試，因為排列組合很多。
// 可試 Dynamic Programming 動態規劃，可把大問題，化成小問題來解
// shivamaggarwal513 提出的解法，直接「函式呼叫函式」慢慢往右解。
int helper(int freq[1001], int i, int* nums, int N, int k) {
    if(i==N) return 1;  // 成功走到最後，終止條件（空集合）是別人的基礎
    int ans = helper(freq, i+1, nums, N, k);  // 問下一格的答案，也就是「不挑選」nums[i]
    // 那，能挑 nums[i] 這個數嗎？
    if( (nums[i]-k<=0 || freq[nums[i]-k]==0) && (nums[i]+k>1000 || freq[nums[i]+k]==0) ){
        // 敵對鄰居沒出現
        freq[nums[i]] += 1; // 就可挑選 nums[i] 這個數
        ans += helper(freq, i+1, nums, N, k);  // 放入 nums[i]後，再問一次答案
        freq[nums[i]] -= 1;  // 再拿掉、不挑選
    }
    return ans;
}
int beautifulSubsets(int* nums, int numsSize, int k) {
    int freq[1001] = {};  // 用來統計 挑選的 nums[i] 出現幾次
    // 數字出現的次數, 都清為0
    return helper(freq, 0, nums, numsSize, k) - 1;  
    // 從0開始往右跑，但題目說，最後要扣掉空集合
}
// case 1120/1307: nums = [10,4,5,7,2,1] k = 3
