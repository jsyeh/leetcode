// LeetCode 861. Score After Flipping Matrix
// 有一堆0和1的matrix，1個move是挑某個 row 或 col 把 0/1 交換
// 可任意次 move。每個 row 是binary表示的數，每個row加起來最大是多少？
// 因沒什麼頭緒，偷看 Editorial 的解說，解釋「從最左邊」逐項flip即可
int matrixScore(int** grid, int gridSize, int* gridColSize) {
    int M = gridSize, N = gridColSize[0];
    for(int i=0; i<M; i++) {
        if(grid[i][0]==0) { // 先處理「最高位」，希望最高位都是1
            for(int j=0; j<N; j++) { // 所以是0時，就整個row flip
                grid[i][j] = 1 - grid[i][j]; 
            }
        }
    }
    int ans = M; // 最高位，對應的bit都變成1，以剝皮法來分析，可先放1*M=M
    for(int j=1; j<N; j++) { // 從「次高位」往「低位」測試
        int now = 0; // 整個直的col數一數有幾個1，再決定是否 flipCol(j)
        for(int i=0; i<M; i++) now += grid[i][j];
        if(M-now>now) now = M-now; // 如果 flip col 後更多1，就flip
        ans = ans * 2 + now;
    }
    return ans;
}

