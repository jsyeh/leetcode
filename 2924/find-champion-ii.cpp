// LeetCode 2924. Find Champion II
// 有 n 隊，edges 有對戰成績（a勝b），請找出冠軍。
// 冠軍「不敗」沒有輸任何一隊。「只能有一隊」是冠軍，不然就 return -1
class Solution {
public:
    int findChampion(int n, vector<vector<int>>& edges) {
        int lost[100] = {}; // 預設值 0
        for(auto edge : edges) {
            lost[edge[1]]++;
        }
        int winner = -1, winnerN = 0;
        for(int i=0; i<n; i++) {
            if(lost[i]==0){
                winner = i;
                winnerN++;
            }
        }
        if(winnerN==1) return winner;
        else return -1;
    }
};
