// 要照著字母順序 order 將 s 的字重新排序
// 不過有些字母不在order裡，那就隨便放
char table[256]={}; //字母序對照表
int cmp(const void *p1, const void *p2) { //照字母序比大小
    return table[*(char*)p1]-table[*(char*)p2];
}
char* customSortString(char* order, char* s) {
    for(int i=0; order[i]!=0; i++){
        table[order[i]]=i; //製作「字母序」的對照表
    }
    int N = strlen(s); //字串長度
    qsort(s, N, sizeof(char), cmp);
    return s;
}
