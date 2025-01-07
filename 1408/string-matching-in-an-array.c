// LeetCode 1408. String Matching in an Array
// words 裡，若某字是另一個字的 substring，就放到答案裡（順序沒關係）
char** stringMatching(char** words, int wordsSize, int* returnSize) {
    int N = 0;
    char** ans = (char**) malloc(sizeof(char*)*wordsSize); // 準備大一點的記憶體
    for(int i=0; i<wordsSize; i++) {
        for(int j=0; j<wordsSize; j++) {
            if(i==j) continue;
            if(strstr(words[j], words[i]) != NULL) {
                ans[N++] = words[i]; // 直接將指標，指到「子字串」的位置
                break;
            }
        }
    }
    *returnSize = N;
    return ans;
}
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

