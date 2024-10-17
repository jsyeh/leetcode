// LeetCode 670. Maximum Swap 把num裡,任2字母最多交換1次,找最大的數
int maximumSwap(int num) {
    int ans = num; //最簡單的答案,就是本身
    char s[20];
    sprintf(s, "%d", num);//把數字「轉成C的字串」
    for(int i=0; s[i]!=0; i++){ //字串的迴圈，左手i
        for(int j=i+1; s[j]!=0; j++){ //字串的迴圈，右手j
            char temp = s[i]; //將 s[i] s[j] 交換
            s[i] = s[j];
            s[j] = temp;
            if(atoi(s) > ans) ans = atoi(s); //轉換成整數，找最大值
            temp = s[i]; // 再將 s[i] s[j] 交換回來
            s[i] = s[j];
            s[j] = temp;
        }
    }
    return ans;
}
