int equalPairs(int** grid, int gridSize, int* gridColSize){
    //看懂題目了，是某個 row 與某個column 竟然全部相同
    //所以用暴力法就可以完成了。但是可能超時：200*200*200 好像還好
    int ans = 0;
    for(int i=0; i<gridSize; i++){
        for(int j=0; j<gridSize; j++){
            int bad=0;
            for(int k=0; k<gridSize; k++){
                if(grid[i][k]!=grid[k][j]){
                    bad=1;
                    break;
                }
            }
            if(bad==0) ans++;
        }
    }
    return ans;
}
