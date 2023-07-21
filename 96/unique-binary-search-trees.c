//可以分解成子問題，再配合組合的次數
//table[i] 表示有 i 個 sorted numbers, 有多少 numTrees
int numTrees(int n){
    int table[n+1];
    table[0] = 1; //有0個數，還是1個數？
    for(int i=1; i<=n; i++){
        table[i] = 0;
        //printf("i:%d\n", i);
        for(int k=0; k<i; k++){ //k:2 表示左邊有2個(0和1)
            int left = table[k];
            int right = (i-k-1>=0) ? table[i-1-k] : 1 ;
            table[i] += left * right;
            //printf("k:%d left:%d right:%d\n", k, left, right);
        }
        //printf("table[%d]: %d\n", i, table[i]);
    }
    return table[n];
}
//table[2]  = 1*2 + 1*1 + 2*1
