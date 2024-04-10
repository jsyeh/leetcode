// 有1000張牌, 一開始全都蓋住。有個翻牌的規則如下
// 1. 把最上面的牌翻開, 拿走
// 2. 再把第2張牌, 移到最後面
// 再繼續以上兩個步驟一直做, 直到牌全部翻走。希望翻出來的牌, 要從小到大跳出來。
// 問: 牌一開始要怎麼放, 才能完成上面的任務, 且翻出的牌是從小到大出來。
// 有點麻煩, 因為好像要倒過來想才行。
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int cmp(const void *p1, const void *p2) {
    return *(int*)p2 - *(int*)p1; // 倒著排序的 cmp 函式
}
int* deckRevealedIncreasing(int* deck, int deckSize, int* returnSize) {
    int ans[2000], ansI = 2000, ansN = 0; // 模擬牌堆
    qsort(deck, deckSize, sizeof(int), cmp); // 倒著將牌放回去
    for(int i=0; i<deckSize; i++){ // 「倒著」將牌放回去
        if(ansN>0) { //如果現在牌堆有牌
            ans[--ansI] = ans[ansI+ansN-1]; // 將最後的牌, 放在最前面
        }
        ans[--ansI] = deck[i]; // 最後抽出來的版, 在最前面
        ansN ++;
    }
    for(int i=0; i<deckSize; i++){ // 把答案放回 desk 以便 return
        deck[i] = ans[ansI+i]; // 使用原來的 deck 陣列來放答案
    }
    *returnSize = deckSize; // 在 C 版本裡, 要把陣列的大小放在 *returnSize 裡
    return deck; // 使用原來的 deck 陣列來放答案
}
