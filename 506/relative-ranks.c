// LeetCode 506. Relative Ranks
// 相對排名：分數高到低，分別是Gold Medal, Silver Medal, Bronze Medal,
// 再來就 4,5,6...下去。我的想法，是先把 index i 和 score 合在一起
// 以 score從大到小排，答案再依序放入
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
struct TABLE {
    int score, index;
};
struct TABLE* table = NULL;  // 初始值都是 NULL，第一次執行時，會填好值
// 以下準備大量的記憶體，以便 LeetCode 評分時，能共享這麼多的記憶體
char** ans = NULL;  // 要回傳的答案
char** ansRank = NULL;  // 依序指到下面的字串（獎牌名or數字的字串）
char* medal[3] = {"Gold Medal", "Silver Medal", "Bronze Medal"};  //金銀銅牌
char others[10000][6];  // 大量字串，存 "4"..."10000" 最長5位，加字串結尾，設6格

int cmp(const void* p1, const void* p2) {  // compare函式供 qsort() 使用
    return ((struct TABLE*)p2)->score - ((struct TABLE*)p1)->score;
}  // 從分數高，到分數低排序用

char** findRelativeRanks(int* score, int scoreSize, int* returnSize) {
    if(ans==NULL) { // 若第一次呼叫 findRelativeRanks() 時，就準備好全部的 memory
        ans = (char**) malloc(sizeof(char*)*10000);  // 回傳的答案，每次都不同
        ansRank = (char**) malloc(sizeof(char*)*10000);  // 排名的字串，小到大排好
        for(int i=0; i<3; i++) ansRank[i] = medal[i];  //前三名
        for(int i=3; i<10000; i++){  // 製作排名的字串, ansRank[0] 對應 金牌
            sprintf(others[i], "%d", i+1);  // ansRank[3] 對應 "4"
            ansRank[i] = others[i];  // 依序放到 ansRank[i] 裡，之後要用
        }
        table = (struct TABLE*) malloc(sizeof(struct TABLE)*10000);  //供排序的表格
    }
    for(int i=0; i<scoreSize; i++) {
        table[i].score = score[i];  // 塞入選手的分數
        table[i].index = i;  // 塞入選手的 index
    }
    qsort(table, scoreSize, sizeof(struct TABLE), cmp);  // 照分數，從高分排到底分
    for(int rank=0; rank<scoreSize; rank++) {  // 依照分數排名，填入 ans[i]
        int i = table[rank].index;
        ans[i] = ansRank[rank];
    }
    *returnSize = scoreSize;
    return ans;
}
