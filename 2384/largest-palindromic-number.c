// 用字串來表示數字，數字超長的，有10^5 位數。
// 那麼能用這個字串，做出的「最大的迴文」是多大呢？
// 使用 greedy 演算法，靠直覺，先把大的數放在外面
// 再慢慢放小的數在裡面即可。
// 但如果只有1個數的話，就只能放中間了
char* largestPalindromic(char* num) {
    int H[10] = {}, len = 0;
    for(int i=0; num[i]!=0; i++){
        H[num[i]-'0']++;
        len++;
    }
    if(H[0]==len) return "0"; //全部都是0時，回傳 "0"

    char * ans = (char*) malloc(sizeof(char)*(len+1));
    int ansN = 0, odd = -1; //-1代表沒有 odd number
    int prefixN = 0;
    for(int i=9; i>=0; i--){
        if(H[i]%2==1 && odd==-1){
            odd = i;
            H[i]--; //降1格，變成偶數
        }
        if(i!=0 || (i==0 && prefixN>0)){ //閉開全部都是0
            for(int k=0; k<H[i]/2; k++){ //有資格放0的話
                ans[prefixN++] = '0' + i;
            }
        }
    }
    //處理奇數的數
    if(odd!=-1){
        ans[prefixN] = '0' + odd;
        for(int i=0; i<prefixN; i++){
            ans[prefixN*2-i] = ans[i];
        }
        ans[prefixN*2+1] = 0;
        return ans;
    }else{
        for(int i=0; i<prefixN; i++){
            ans[prefixN*2-1-i] = ans[i];
        }
        ans[prefixN*2] = 0;
        return ans;
    }
}

