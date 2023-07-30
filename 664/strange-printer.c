//這題DP的解法，table[left][right] 對應子問題 left...right(包含)要印幾次
// 再利用迴圈 k 來拆解問題，若 s[left] == s[k] 那可再拆成半：
// table[left][right] = table[left][k-1] + table[k+1][right];
//因為字串長度 <=100 所以陣列應該夠用
int strangePrinter(char * s){
    int N = strlen(s);
    int table[N][N]; //table[left][right]: s[left]...s[right] 要幾次印出來
    for(int left=0; left<N; left++){ //left s[left]
        for(int right=0; right<N; right++){ //right (包含) s[right]
            if(left==right) table[left][right] = 1; //只有1個字母，就印1 
            else if(left+1==right){ 
                //2個字母：相鄰2字母相同，一起印；不同就分2次印。
                if(s[left]==s[right]) table[left][right] = 1;
                else table[left][right] = 2;
            }
            else table[left][right] = INT_MAX; //表示沒有值，隨時能被更新取代
        }
    }
    //左右邊界的距離，從小到大慢慢增加。前面已解決 j=i+1的部分，接下來是 j=i+2 ...
    for(int dist=2; dist<N; dist++){ //dist表示 i...j的距離, i+dist==j
        for(int left=0; left+dist<N; left++){ //i是左邊界
            int right = left + dist; //j是右邊界()包含)
            table[left][right] = table[left+1][right] + 1;
            //最差的狀況，就是再多印一次嘛

            for(int k = left+1; k<right; k++){ // left < 中間的k < right
                //s[left] 與 s[k] 逐一比較
                if(s[left]==s[k]){
                    //如果相同，那有可能左半邊 + 右半邊 的答案 是可能的答案
                    // 把 s[k] 當成是 s[left]...s[right] 殘留 s[left]的值
                    int now = table[left][k-1] + table[k+1][right];
                    if(now<table[left][right]) table[left][right] = now;
                    //更小的值，那就更新
                }
            }
            if(s[left]==s[right]){
                int now = table[left][right-1]; //答案可能與少1格的相同
                if(now<table[left][right]) table[left][right] = now;
            }
        }
    }
    return table[0][N-1];
}
