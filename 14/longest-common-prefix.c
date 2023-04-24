char * longestCommonPrefix(char ** strs, int strsSize){
    int a = 0;
    if(strsSize==0) return "";
    while( strs[0][a] ){
        for(int i=1; i<strsSize; i++){
            if(strs[0][a]!=strs[i][a]){
                strs[0][a]=0;
                return strs[0];
            }
        }
        a++;
    }
    strs[0][a]=0;
    return strs[0];
}
