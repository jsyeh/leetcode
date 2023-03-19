class Solution {
    public int[] evenOddBit(int n) {
        //ArrayList<Integer> bits = new ArrayList<Integer>();
        int i=0, even=0, odd=0;
        while(n>0){
            //bits.add(n%2);
            if(n%2==1 && i%2==0) even++;
            if(n%2==1 && i%2==1) odd++;
            n = n / 2;
            i++;
        }
        int [] ans = new int[2];
        ans[0] = even;
        ans[1] = odd;
        return ans;
    }
}
