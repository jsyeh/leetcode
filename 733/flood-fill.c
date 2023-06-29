/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
void helper(int** image, int M, int N, int i, int j, int old, int color){
    if(i<0 || j<0 || i>=M || j>=N) return;

    if(image[i][j]==old) image[i][j]=color;
    else return;

//printf("%d %d\n", i, j);
    helper(image, M, N, i+1, j, old, color);
    helper(image, M, N, i-1, j, old, color);
    helper(image, M, N, i, j+1, old, color);
    helper(image, M, N, i, j-1, old, color);
}

int** floodFill(int** image, int imageSize, int* imageColSize, int sr, int sc, int color, int* returnSize, int** returnColumnSizes){
    int M = imageSize, N = imageColSize[0];

    //想要改變的話，才要呼叫 helper()
    if(color!=image[sr][sc]) helper(image, M, N, sr, sc, image[sr][sc], color);
    //如果要改變的就已經改變好了，就什麼都不用算

    *returnSize = M;
    *returnColumnSizes = imageColSize;
    return image;
}
