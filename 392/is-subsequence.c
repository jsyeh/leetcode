bool isSubsequence(char * s, char * t){
    //s 是短的 t是長的
    int i=0, k=0;
    while(s[i]!=0 && t[k]!=0){
        if(s[i]==t[k]){
            i++;//相同，各進一步
            k++;
        }else k++; //只有長的走一步
    }
    if(s[i]==0) return true; //短的 s[i] 有走到最後，表示成功比對完成
    else return false;
}
