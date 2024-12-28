// LeetCode 3248. Snake in Matrix
// n x n 的正方形（矩陣）一開始在左上角，commands 移動方向，問最後位置
int finalPositionOfSnake(int n, char** commands, int commandsSize) {
    int i = 0, j = 0;
    for(int k=0; k<commandsSize; k++) {
        if(commands[k][0]=='U') i--;
        else if(commands[k][0]=='R') j++;
        else if(commands[k][0]=='D') i++;
        else j--;
    }
    return i * n + j;
}
