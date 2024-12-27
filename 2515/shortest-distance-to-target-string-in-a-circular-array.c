// LeetCode 2515. Shortest Distance to Target String in a Circular Array
// 有100個字串，你從 startIndex 出發，可往右、往左，最快多久可遇到 target 字串
int closetTarget(char** words, int wordsSize, char* target, int startIndex) {
    for(int i=0; i<wordsSize; i++){
        int i1 = (startIndex+i)%wordsSize; // 往右的 index 
        int i2 = (startIndex+wordsSize-i)%wordsSize; // 往左的 index
        if(strcmp(words[i1], target) == 0) return i; // 往右有找到
        if(strcmp(words[i2], target) == 0) return i; // 往左有找到
    }
    return -1; // 找不到
}
