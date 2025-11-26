// LeetCode 976. Largest Perimeter Triangle
// 要用 nums 裡的棒子長度, 組合出「三角形」兩邊和>第3邊
class Solution {
public:
    int largestPerimeter(vector<int>& nums) {
        sort(nums.begin(), nums.end()); // 排序(又快又好)
        //for (int i=nums.size()-1; i>=0; i--) { // 用迴圈, 到大小都試一次
        // 倒過來的迴圈
        //    cout << nums[i] << " "; // 印出大到小的數
        //} // 先印出「大到小」等一下,這3行會刪掉 (可留下上面3行註解, 因為可以理解「反過來的迴圈」)
        for (int i=nums.size()-1; i>=2; i--) { // 迴圈有稍修改, nums[i] vs. -1,-2
            if (nums[i] < nums[i-1] + nums[i-2]) return nums[i]+nums[i-1]+nums[i-2];
            // 如果順利「兩邊和大於第三邊」 就把我們的周長加起來, 當成答案
        }

        return 0; // 找不到任何「合法」的三角形,就 return 0
    }
};
