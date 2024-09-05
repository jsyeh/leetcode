// LeetCode 2710. Remove Trailing Zeros From a String
// 把 num 右邊的0刪光光。
char * removeTrailingZeros(char * num){
    int N = strlen(num);
    for(int i=N-1; i>=0; i--){
        if(num[i]=='0') num[i] = 0; //變成字串結尾
        else return num;
        //只要字母「不是'0'」就中斷迴圈。右邊已裁掉，當成答案
    }
    return num; // 只是寫好玩的，應不會變成這樣啦（0都被裁光）
}

