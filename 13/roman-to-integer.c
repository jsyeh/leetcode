int romanToInt(char * s){
    char * symbol = "IVXLCDM";
    int v[] = {1,5,10,50,100,500,1000}; //value

    int ans = 0;
    int N = strlen(s);
    //int d[N]; //將比對出來的value index 存起來，方便確認是否有倒過來
    int prev = 7;//確保一定比較大。有了 prev 就不需要上面的 d[i] 了
    for(int i=0; i<N; i++){
        for(int k=0; k<7; k++){
            if(symbol[k]==s[i]){
                //d[i] = k;//找到對應的index值
                if(k>prev){ //倒過來的狀況，要做減法
                    ans = ans + v[k] - v[prev] - v[prev];//多減回
                }else ans = ans + v[k];
                prev = k; //記下對應的index值，下一輪要比較
                break;
            }
        }
    }
    return ans;
}
