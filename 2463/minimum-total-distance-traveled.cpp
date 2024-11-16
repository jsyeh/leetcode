// LeetCode 2463. Minimum Total Distance Traveled
// 機器人在 robot[i] 位置，要進工廠 factory[j] 維修
// 工廠 factory[j] 有它的位置、容量，不能超過維修容量。
// 問機器人進廠維修「移動」的「最小距離和」是多少
class Solution {
public:
    vector<int> robot2;
    vector<vector<int>> factory2;
    int R, F; // 機器人數量、工廠數量（終止條件會用到）
    long long table[101][101][101];
    // 考慮機器人i、工廠 j，其中工廠 j 已用掉 k 個維修容量，問移動的「最小距離和」
    long long helper(int i, int j, int k) {
        if(i==R) return 0; // 終止條件：機器人全部處理完，最簡單的終止條件，距離是0
        if(j==F) return std::numeric_limits<long long int>::max(); // 終止修條件：工廠不夠用，沒正常結束，就失敗
        if(table[i][j][k]!=-1L) return table[i][j][k];
        if(k==factory2[j][1]) {// 抱歉，工廠 j 維修容量不足（已用掉 k 個維修容量，工廠滿了，無法再維修）
            table[i][j][k] = helper(i, j+1, 0);
            return table[i][j][k]; // 只能再開新工廠 j+1
        } else { // 工廠 j 的維修容量還夠，那就有2種可能：
            // (1) 使用工廠 j 的第 k+1 個維修容量。機器人 i 在工廠 j 維修，計算距離
            long long ans1 = helper(i+1, j, k+1);//還要再 + abs(robot2[i]-factory2[j][0]);

            long long ans2 = helper(i, j+1, 0); // (2) 不管舊工廠，再開新工廠 j+1 加入維修行列，繼續問
            if(ans1==std::numeric_limits<long long int>::max()) return table[i][j][k] = ans2;
            ans1 += abs(robot2[i]-factory2[j][0]);
            if(ans1<ans2) table[i][j][k] = ans1;
            else table[i][j][k] = ans2; // 以上2種可能，看誰的距離最小
            return table[i][j][k];
        }
    }
    long long minimumTotalDistance(vector<int>& robot, vector<vector<int>>& factory) {
        sort(robot.begin(), robot.end()); // 左到右排序
        sort(factory.begin(), factory.end()); // 左到右排序
        R = robot.size();
        F = factory.size();
        for(int i=0; i<=R; i++) {
            for(int j=0; j<=F; j++) {
                for(int k=0; k<=R; k++) {
                    table[i][j][k] = -1L; // 初始值
                }
            }
        }
        robot2 = robot;
        factory2 = factory;
        return helper(0, 0, 0); // 從 robot 0, factory 0 開始處理   
    }
};

