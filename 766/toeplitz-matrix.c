// LeetCode 766. Toeplitz Matrix
// 矩陣的「每一條斜線」值都相同，叫 Toeplitz 矩陣。檢試 matrix 是不是
bool isToeplitzMatrix(int** matrix, int matrixSize, int* matrixColSize) {
    int M = matrixSize, N = matrixColSize[0];
    for(int i=0; i<M-1; i++) {
        for(int j=0; j<N-1; j++) {
            if(matrix[i][j] != matrix[i+1][j+1]) { // 若斜線不相同
                return false; // 就不是
            }
        }
    }
    return true; // 成功檢測完，就是！
}
