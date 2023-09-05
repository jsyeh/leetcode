class Solution {
public:
    bool judgeCircle(string moves) {
        int x = 0, y = 0;
        char[] dir = "RLUD";
        int dx[] = {1, -1, 0, 0};
        int dy[] = {0, 0, -1, 1};
        int N = moves.length();
        for(int i=0; i<N; i++){
            for(int d=0; d<4; d++){
                if(moves[i]==dir[d]){
                    x += dx[d];
                    y += dy[d];
                    break;
                }
            }
        }
        if(x==0 && y==0) return true;
        else return false;
    }
};
