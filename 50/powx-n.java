class Solution {
    public double myPow(double x, int n) {
        if(n==0) return 1;
        if(n==-2147483648){
            return myPow(1/x/x, -(n/2));
            //因為 test data 多了 case 305/306: 1.0000000000001 -2147483648
            //這個case太刁鑽了，答案還沒變成0, 而是變成 0.99979
            //所以程式需要做修改
        }
        if(n<0){
            x = 1/x;
            n = -n;
        }

        if(n%2==0) return myPow(x*x, n/2);
        else return x*myPow(x*x, n/2);
    }
}//Case4: 2.00000 -2147483648
//Case5: -1.00000 -2147483648
//case 305/306: 1.0000000000001 -2147483648
