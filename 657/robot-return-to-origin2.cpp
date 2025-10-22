// LeetCode 657. Robot Return to Origin
// 模擬機器人走路
// 'U' up往上, 'D' down往下, 'L' left往左, 'R'right往右
class Solution {
public:
    bool judgeCircle(string moves) {
        int x = 0, y = 0; // 一開始的位置, 在 (0,0)
        //for (int i=0; i<moves.length(); i++) { // 傳統的 for 迴圈
        //    char c = moves[i];             // 取出字串裡第i個字母
        for (char c : moves) { // C++ 進階迴圈
            if (c=='U') { // up往上
                y++;
            } else if (c=='D') { // down往下
                y--;
            } else if (c=='L') { // left往左
                x--;
            } else if (c=='R') { // right往右
                x++;
            }
        } // 離開迴圈後
        if (x==0 && y==0) return true;
        else return false;
    }
};
