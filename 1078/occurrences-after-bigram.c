// LeetCode 1078. Occurrences After Bigram
// Bi-gram 是二元組，如果 first 接 second 再接 third 的話，third 是答案
char* ans[1000]; // global 陣列（放答案的指標，它不會不見，就不用準備memory)
char** findOcurrences(char* text, char* first, char* second, int* returnSize) {
    char *prev = text;
    int wordN = 0;
    for(int i=0; text[i]!=0; i++){ // 先斷字
        if(text[i]==' '){
            text[i] = 0; // 變成字串結尾
            ans[wordN++] = prev;
            prev = &text[i+1];
        }
    }
    ans[wordN++] = prev; // 最後1個字

    int ansN = 0;
    for(int i=0; i<wordN-2; i++){
        if(strcmp(ans[i],first)==0 && strcmp(ans[i+1],second)==0){
            ans[ansN++] = ans[i+2];
        }
    }

    *returnSize = ansN;
    return ans; // 回收再利用，直接拿來放答案
}
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

