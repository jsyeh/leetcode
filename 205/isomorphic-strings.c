bool isIsomorphic(char * s, char * t){
    int N1 = strlen(s), N2 = strlen(t);
    if(N1!=N2) return false; //長度不一樣, 不合格

    char table1[256] = {}; //對照表 c1 => c2
    char table2[256] = {}; //對照表 c2 => c1

    for(int i=0; i<N1 ; i++) {
        char c1 = s[i], c2 = t[i];
        if(table1[c1]==0 && table2[c2]==0){
            table1[c1] = c2; //兩個都空,可以做對照表
            table2[c2] = c1;
        }

        if(table1[c1]!=c2) return false;//不合格
        if(table2[c2]!=c1) return false;//不合格
    }

    return true; //合部檢查都合格
}
//程式解題,分成5個層次
//1. 英文看不懂
//2. 英文就算看懂,但題目還是不懂(翻譯無效,看input/output會有幫助)
//3. 了解題目,但不會寫(沒有方向)
//4. 知道方向,會寫,但寫出來是錯的)
//5. 寫出來了
