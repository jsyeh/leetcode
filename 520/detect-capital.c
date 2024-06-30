// 希望字是「全大寫」、「全小寫」、「首字大寫」的任一種 True
// 其他都 False
bool detectCapitalUse(char* word) {
    bool allLower=true, allUpper=true, cap=true; //3種都還可能
    if(isupper(word[0])) allLower=false; //大寫
    else {  // 小寫
        allUpper = cap = false;
    }
    for(int i=1; word[i]!=0; i++){
        if(isupper(word[i])){  //大寫
            allLower = cap = false; //這些就沒機會了
        }else{  // 小寫
            allUpper = false; //這個就沒機會了
        }
        if((allLower || allUpper || cap)==false) return false;
    }
    return true; //經過層層檢查，都沒提早失敗，就是成功
}
