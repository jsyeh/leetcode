// LeetCode 3208. Alternating Groups II
// colors 有一堆0和1，繞成圈。請問有幾種「長度為k」的片段，是0、1交錯？
class Solution {
public:
    int numberOfAlternatingGroups(vector<int>& colors, int k) {
        int N = colors.size(), start = -N+1, ans = 0;
        for(int i=N-k+1; i<N; i++) { // 先處理「倒數」的量
            if(colors[i-1]==colors[i]) start = i - N; // 可看成「環狀」負數的部分
        }
        if(colors[N-1]==colors[0]) start = 0; // 但在跨「邊界」時，要另外處理
        if(0-start >= k-1) ans++; // 第0項，在倒數 k-1 項都沒問題

        for(int i=1; i<N; i++) { // 最後「正常處理
            if(colors[i-1]==colors[i]) start = i;
            if(i-start >= k-1) ans++;
        }
        return ans;
    }
};
