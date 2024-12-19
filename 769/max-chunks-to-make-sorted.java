// LeetCode 769. Max Chunks To Make Sorted
// 把 arr 分段斷開，分別sort() 再合起來，要是 sorted，問能分幾段
// 因為數字是 0..n-1 去排列，Hint 1 說前i項的最大值是i就合理
class Solution {
    public int maxChunksToSorted(int[] arr) {
        int ans = 0, nowMax = 0;
        for(int i=0; i<arr.length; i++) {
            if(arr[i]>nowMax) nowMax = arr[i];
            if(nowMax==i) ans++;
        }
        return ans;
    }
}
