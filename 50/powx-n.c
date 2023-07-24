//因為 n 超級大，所以不能用for迴圈慢慢乘
//可以利用函式呼叫函式，將n拆成很多數相乘，每次切一半
double myPow(double x, int n){
    //邊界條件
    if(n==0) return 1; //任何數的0次方，都是1
    if(n==1) return x; //任何數的1次方，就是本身

    if(n<0){ //如果是負的，x改成成倒數即可
        if(n==-2147483648) return myPow(1/x/x, -(n/2)); 
        //上面是特殊狀況，因為 -2147483648 再取負，會超過 INT_MAX overflow
        //所以要在前面另外處理，多做幾步，幫它把n變小
        
        return myPow(1/x, -n);
    }
    if(n%2==0){ //n拆一半
        return myPow(x*x, n/2);
    }else{ //因為是奇數，n拆一半後，還會掉個1， 所以 x 要乘上去
        return x * myPow(x*x, n/2);
    }
}
//case 305/306: 1.0000000000001 -2147483648
//這個case太刁鑽了，答案還沒變成0, 而是變成 0.99979
//所以之前我的 Java 版本程式，也會無法通過！

//測試資料不會是 0 -2147483648 因為
//0 cannot be raised to a non-positive power
//題目規定，不能有0的負數次方，因為會有無限大的問題

