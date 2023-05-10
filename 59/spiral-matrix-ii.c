/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** generateMatrix(int n, int* returnSize, int** returnColumnSizes){
    int ** ans = (int**)malloc(sizeof(int*)*n);
    *returnColumnSizes = (int*)malloc(sizeof(int)*n);
    for(int i=0; i<n; i++){
        ans[i] = (int*)malloc(sizeof(int)*n);
        (*returnColumnSizes)[i] = n;
    }
    *returnSize = n;

    int dir = 0;
    int di[4] = {0,1,0,-1};
    int dj[4] = {1,0,-1,0};
    int i = 0, j = 0;
    int left = 0, right = n-1, up = 1, down = n-1;
    for(int k=1; k<=n*n; k++){
        ans[i][j] = k;
        if(dir==0 && j==right){
            dir = 1;
            right--;
        }else if(dir==1 && i==down){
            dir = 2;
            down--;
        }else if(dir==2 && j==left){
            dir = 3;
            left++;
        }else if(dir==3 && i==up){
            dir = 0;
            up++;
        }
        i += di[dir];
        j += dj[dir];
    }
    return ans;
}
