// LeetCode 874. Walking Robot Simulation
// 機器人一開始在(0,0)位置，command[i] -2:左轉 -1右轉 1..9前進，模擬機器人走動
// 遇到「障礙」會卡在原地，問「機器人最遠走多遠」，距離要記得「平方」 a*a+b*b=c*c 當結果
class Solution {
public:
    int robotSim(vector<int>& commands, vector<vector<int>>& obstacles) {
        unordered_set<int> hashmap;  // 為快速「碰撞偵測」，使用 hashmap
        for(vector<int> obstacle : obstacles) {
            hashmap.insert((obstacle[0]<<15) + obstacle[1]);
        } // 把「座標」的 x,y 換算成 x*2^15 + y 的整數
        int d = 0;  // 0向北+Y，1向東+X，2向南-Y，3向西-X
        int dx[4] = {0, 1, 0, -1}, dy[4] = {1, 0, -1 ,0};
        int x = 0, y = 0, ans = 0; // x,y 是一開始「機器人」的座標。
        for(int command : commands) {
            if(command==-2) d = (d+3) % 4; // 左轉
            else if(command==-1) d = (d+1) % 4; // 右轉
            else{ // 前進 1...9 步
                for(int k=0; k<command; k++) {
                    x += dx[d];
                    y += dy[d];
                    if(hashmap.find((x<<15)+y) != hashmap.end()) { // 有找到，表示「是障礙」
                        x -= dx[d];
                        y -= dy[d];
                    }
                    ans = max(ans, x*x+y*y); // ans 是機器人「最遠」的距離，以「平方」來呈現
                }
            }
        }
        return ans;
    }
};
