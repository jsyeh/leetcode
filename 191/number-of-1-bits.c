
int hammingWeight(uint32_t n) {
    int ans=0;
    while(n>0){ //數字還沒剝完,就繼續做
        int now = n%2; //剝一層皮
        if(now==1) ans++; //剝下來的皮,有幾個1
        n = n / 2; //數字又變更小了
    }
    return ans;
}
    //剝皮法
    /*1234
       4
    123
      3
    12
     2
    1
    
    0
    */
