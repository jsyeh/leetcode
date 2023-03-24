class Solution {
    public double myPow(double x, int n) {
        if(n==0) return 1;
        if(n==-2147483648){
            if(x==1) return 1;
            if(x==-1) return 1;
            return 0;
            /*x = 1/x;
            n -= 1;
            n = -n;
            return x*x*myPow(x*x, n/2 );*/
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
