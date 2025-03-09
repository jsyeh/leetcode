// LeetCode 3208. Alternating Groups II
// colors 有一堆0和1，繞成圈。請問有幾種「長度為k」的片段，是0、1交錯？
class Solution {
public:
    int numberOfAlternatingGroups(vector<int>& colors, int k) {
        int N = colors.size();
        int combo = 1, ans = 0, prev = colors[0];
        for(int i=1; i<N+k-1; i++) {
            if(colors[i%N]==prev) combo = 1;
            else combo++;
            if(combo>=k) ans++;
            prev = colors[i%N];
        }
        return ans;
    }
};
