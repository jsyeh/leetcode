// LeetCode 3248. Snake in Matrix
// n x n 的正方形（矩陣）一開始在左上角，commands 移動方向，問最後位置
class Solution {
public:
    int finalPositionOfSnake(int n, vector<string>& commands) {
        int i = 0, j = 0;
        for(string command : commands) {
            if(command=="UP") i--;
            else if(command=="RIGHT") j++;
            else if(command=="DOWN") i++;
            else j--;
        }
        return i * n + j;
    }
};
