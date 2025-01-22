// LeetCode 1668. Maximum Repeating Substring
// 這題好難想。Solutions 有人用迴圈暴力做(測不同長度），就簡單了
int maxRepeating(char* sequence, char* word) {
    int ans = 0;
    int S = strlen(sequence), W = strlen(word);
    for(int i=0; i<S-W+1; i++) {
        int count = 0;
        while(strncmp(sequence+i+W*count, word, W)==0) {
            count++; // 有相同的話，比較「再往右移 W*count 格」
        }
        if(count>ans) ans = count;
    }
    return ans;
}
