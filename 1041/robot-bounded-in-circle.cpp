//(1) 這是模擬題，看機器人會走到哪裡、向哪個方向
//(2) 是否會在有限的空間 vs. 是否會發散、到無限大的地方
// 其實看它的方向，如果方向有回來，就True。如果方向轉90度，也會是True
class Solution {
public:
    bool isRobotBounded(string instructions) {
        int dx[] = {1,0,-1,0}; //4個方向的移動
        int dy[] = {0,1,0,-1}; //4個方向的移動
        int x = 0, y = 0, dir = 0; //初始位置、初始方向
        for(int i=0; i<instructions.length(); i++) {
            char c = instructions[i];
            if(c=='L') dir = (dir+1)%4;
            if(c=='R') dir = (dir+3)%4;
            if(c=='G'){
                x += dx[dir];
                y += dy[dir];
            }
        }
        if(x==0 && y==0) return true; //留在原地的話，一定可以
        else if(dir==0) return false; //沒留在原地，而向同一方向，會持續移動
        else return true; //只要轉動方向，就會循環
    }
};
