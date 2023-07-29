//因為 n <= 10^9, 所以不能用迴圈慢慢模擬。（有人實驗後，說4800之後，答案就穩定為1）
// If the remaining volume of soup is not enough to complete the operation, we will serve as much as possible
// 意思是soup不夠用的話，就用光它沒關係
double table[5000][5000] = {}; //global變數，預設值是0
double prob(int a, int b){
    if(a<=0 && b>0) return 1;
    if(a<=0 && b<=0) return 0.5;
    if(a>0 && b<=0) return 0;
    //以上是3種終止條件

    if(table[a][b]!=0) return table[a][b];
    //簡單的函式呼叫函式，可能會TLE超時，要加上table去查表
    double type1 = prob(a-100, b);
    double type2 = prob(a-75, b-25);
    double type3 = prob(a-50, b-50);
    double type4 = prob(a-25, b-75);

    table[a][b] = 0.25 * (type1+type2+type3+type4);
    return table[a][b];
}
double soupServings(int n){
    if(n>=5000) return 1; //討論區有人說 n>4800 答案就是1，經測試果然如此
    return prob(n, n);
}
