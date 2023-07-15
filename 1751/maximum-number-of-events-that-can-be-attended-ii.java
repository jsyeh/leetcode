//這題有夠難。我能解簡化版本 1353. Maximum Number of Events That Can Be Attended
//但我這題就真的沒有頭緒。Editorial 和 Solutions 都有人講是 DP + Binary Search
//我就參考 mr_kamran 的解法，也就是 Solutions 裡很多人投票的方法
//https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/solutions/3766452/c-faster-than-95-explained-2d-dp-memoization-binary-search-clean-code/
class Solution {
    public int maxValue(int[][] events, int k) {
        Arrays.sort(events, (a,b)->a[0]-b[0]); //照 event[i][0] 來排序
        int N = events.length;
        int[][] table = new int[N+1][k+1];
        //table[i][j] 表示 考慮過 i 個 events, 其中挑了 j 個 events
        for(int i=0; i<=N; i++){
            for(int j=0; j<=k; j++){
                table[i][j] = -1; //-1表示還沒有處理過
            }
        }
        int ans = helper(0, events, k, table);
        //小幫手，幫忙算答案，倒過來，index走回最前面 & 挑 k個events, 最好的答案
        return ans;
    }
    int helper(int i, int[][] events, int k, int[][] table) {
        if(i<0 || i>=events.length || k==0) return 0;
        //不合理的 i 答案是0。如果挑0個event,答案也是0
        if(table[i][k] != -1) return table[i][k]; //之前算過（不是-1），就直接回傳

        //如果我挑了第i個事件，那它結束後，可以接哪一個事件？
        //也就是 i+1 之後的 event 中，哪一個以後時間就不會衝突？ 
        int index = BinarySearch(i+1, events, events[i][1]);
        //index之後的時間都不衝突，很好，試試看

        //c1是挑選 event i 對應的價值(events[i][2] + 它結束後，不衝突的案子的最高價值)
        //c2是不使用 event i 跳過後，對應的價值(再問下一個)
        int c1 = events[i][2] + helper(index, events, k-1, table);
        int c2 = helper(i+1, events, k, table);
        if(c1>c2) table[i][k] = c1;
        else table[i][k] = c2;

        return table[i][k];
    }
    //利用 Binary Search 找 index 之右「開始時間不會衝突」的位置
    int BinarySearch(int index, int[][] events, int endTime) {
        int left = index;
        int right = events.length-1;
        int ans = -1;
        while(left<=right) {
            int mid = (left + right) / 2;
            if(events[mid][0] > endTime) { //開始時間在 value 之後
                ans = mid;
                right = mid - 1;
            } else left = mid + 1;
        }
        return ans;
    }
}
