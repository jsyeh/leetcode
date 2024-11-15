// LeetCode 1574. Shortest Subarray to be Removed to Make Array Sorted
// 刪掉「某一段」後，陣列變成「小到大排好」。
// 參考votrubac的解法，先把右端的最長先找出來，再用「毛毛蟲」法，滑動比對。
class Solution {
public:
    int findLengthOfShortestSubarray(vector<int>& arr) {
        int N = arr.size();
        int left = 0, right = N - 1; // 左邊界、右邊界放好
        while(right>0 && arr[right-1] <= arr[right]) right--; // 先「右界往左滑」
        
        int ans = right;
        while(left<right && (left==0 || arr[left-1]<=arr[left])) { // 再「左界往右滑」
            while(right<N && arr[left] > arr[right]) { // 左界、右界 無法照大小順序接起來
                right++; // 就「右界往右滑」
            }
            ans = min(ans, right-left-1); // 更新答案
            left++;
        }
        return ans;
    }
};

