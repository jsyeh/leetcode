/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* spiralOrder(int** matrix, int matrixSize, int* matrixColSize, int* returnSize){
    int M = matrixSize, N = matrixColSize[0];
    *returnSize = N*M;
    int * ans = (int*) malloc(sizeof(int)*M*N);
    

    int dir = 0; //0:right, 1:down, 2:left, 3:up
    int dx[4] = {1,0,-1,0};
    int dy[4] = {0,1,0,-1};
    int right=N-1, left=0, up=1, down=M-1;
    int i=0, j=0, ansN=0;
    while(ansN < N * M){
        printf("i:%d j:%d\n", i, j);
        printf("%d ", matrix[i][j]);
        ans[ansN++] = matrix[i][j];
        if(dir==0 && j==right){
            right--;
            dir=1;
        }else if(dir==1 && i==down){
            down--;
            dir=2;
        }else if(dir==2 && j==left){
            left++;
            dir=3;
        }else if(dir==3 && i==up){
            up++;
            dir=0;
        }
        i+=dy[dir];
        j+=dx[dir];
    }
    return ans;
}
//case 4/25: [[3],[2]]
