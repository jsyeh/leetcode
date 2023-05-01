bool searchMatrix(int** matrix, int matrixSize, int* matrixColSize, int target){
    int M = matrixSize, N = matrixColSize[0];
    int left = 0, right = M*N; //右不包含

    while(left<right){
//printf("left:%d right:%d\n", left, right);
        int mid = (left+right)/2;
//printf("mid:%d\n", mid);
        int i = mid/N, j=mid%N;
        if(matrix[i][j]==target) return true;
        if(matrix[i][j]>target){ //退
//printf("退\n");
            right = mid;
        }else{ //進
//printf("進\n");
            left = mid+1;
        }
    }
    return false;
}
