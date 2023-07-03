bool buddyStrings(char * s, char * goal){
    //全相同:true
    //只有兩個不同，且可以swap: true
    int N = strlen(s), N2 = strlen(goal);
    if(N!=N2) return false;

    int H1[26]={}, H2[26]={};
    int ii[3];//用來記憶bad的數量
    int bad = 0;
    for(int i=0; i<N; i++){
        H1[s[i]-'a']++;
        H2[goal[i]-'a']++;
        if(s[i]!=goal[i]){
            if(bad>=2) return false;
            ii[bad] = i;
            bad++;
        }
    }
    if(bad==0) { //如果字串完全相同，就需要有「重覆的字母」才行
        for(int i=0; i<26; i++){
            if(H1[i]>=2) return true;
        }
        return false; //不幸都找不到重覆的字母，就無法swap而失敗
    }
    if(bad==2 && s[ii[0]]==goal[ii[1]] && s[ii[1]]==goal[ii[0]]) return true;
    return false;
}
