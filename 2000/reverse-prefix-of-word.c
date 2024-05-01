char* reversePrefix(char* word, char ch) {
    for(int i=0; word[i]!=0; i++) {  // 字串的 for迴圈
        if(word[i]==ch) {  // 找到 ch 所在的位置
            for(int k=0; k<=i/2; k++) {  // 只要迴圈做一半即可全部反過來。
                int temp = word[k];  // 把前面反過
                word[k] = word[i-k];
                word[i-k] = temp;
            }
            break; //做完,就離開迴圈
        }
    }
    return word;
}

