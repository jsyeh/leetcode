//觀察 vortrubac 的解法, 利用 table[i][j] 表示 從左到右,第i刀 第j刀 最好的答案
class Solution {
public:
    int table[102][102] = {};//最多100刀, 加上 0 及 N 的兩邊兩刀, 就102個格子

    int minCost(int n, vector<int>& cuts) {
        cuts.push_back(0);//然後先多了 0 左邊界 及 n 右邊界 的兩邊兩刀
        cuts.push_back(n);
        sort(cuts.begin(), cuts.end());
//        for(int c : cuts){
//            printf("%d ", c);
//        }
        return dfs(cuts, 0, cuts.size()-1 );//剛好最左、最右的邊界index, 要查 dfs() return 的值
    }

    int dfs(vector<int>& cuts, int i, int j) { //左手i, 右手j
//printf("i:%d j:%d\n", i, j);
        if(i>j) return 0;//不對的切法
        if(i==j) return 0;
        if(j==i+1) return 0;//cuts[j]-cuts[i];

        if(table[i][j]!=0) return table[i][j];
        //因為 table[i][j] 不可能為0, 所以如果不是初始值0的話, 代表table[i][j] 有算過

        int ans = dfs(cuts, i, i+1) + dfs(cuts, i+1, j); //拆成兩個子問題
        for(int k=i+2; k<j; k++) {
            int temp = dfs(cuts, i, k) + dfs(cuts, k, j);
            if(temp<ans) ans = temp;;
        }
        table[i][j] = ans + (cuts[j]-cuts[i]);
        return table[i][j];
    }
};
//case 55/100: 774 [174,726,424,757,53,706,364,8,429,163,290,476,245,454,480,197,139,208,301,568,241,246,592,162,170,89,591,341,548,574,611,100,105,274,270,83,461,492,652,177,702,338,69,273,59,741,442,184,294,210,394,230,576,392,34,192,734,78,16,604,285,282,550,388,351,503,629,526,131,508,662,374,497,123,470,520,430,637,561,133,617,334,642,577,466,699,306,300,304,42,398,344,521,661]
//可能是printf()印太多了
