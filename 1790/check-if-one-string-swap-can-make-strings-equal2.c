// LeetCode 1790. Check if One String Swap Can Make Strings Equal
// 字串 s1 最多「只調動2個字母」的位置，能不能變成 s2
bool areAlmostEqual(char * s1, char * s2){
    int a = -1, b = -1; // 可記錄備份 2個 index（為避免太多i，改叫 a 跟 b）
    for(int i=0; s1[i]!=0; i++) { // 字串迴圈，逐一比較
        if(s1[i] != s2[i]) { // 若字母不相同
            if(b != -1) return false; // 兩個 index 都用完了，就超過了
            b = a; // 如果沒有超過的話，就把 a 備份到 b
            a = i; // 再把 i 移到 a。這樣就能將 i 及 a 備份到 a 及 b
        }
    }
    if(a==-1) return true; // 都沒有任何 index 被備份，代表「完全相同」，成功
    if(b!=-1 && s1[a]==s2[b] && s1[b]==s2[a]) return true; 
    // b也用到了，代表「備份」了兩個2個index。若交換後相同，那也是成功

    return false;
}
