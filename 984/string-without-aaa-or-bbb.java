class Solution {
    public String strWithout3a3b(int a, int b) {
        String ans = "";
        int contA=0, contB=0;
        while(a>0 || b>0){
            if(contA==2){
                ans += 'b';
                b--;
                contA=0;
                contB=1;
            } else if(contB==2){
                ans += 'a';
                a--;
                contA=1;
                contB=0;
            }else if(a>=b){
                ans += 'a';
                a--;
                contA++;;
                contB=0;
            } else {
                ans += 'b';
                b--;
                contB++;
                contA=0;
            }
        }
        return ans;
    }
}
