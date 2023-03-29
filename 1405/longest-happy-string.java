class Solution {
    String ans = "";
    public String longestDiverseString(int a, int b, int c) {

        while(true) {
            //System.out.println(ans);
            if(prevAns("aa")){
                if(b>=c && b>0){
                    ans+="b";
                    b--;
                }else if(c>=b && c>0){
                    ans+="c";
                    c--;
                }
            }else if(prevAns("bb")){
                if(a>=c && a>0){
                    ans+="a";
                    a--;
                }else if(c>=a && c>0){
                    ans+="c";
                    c--;
                }
            }else if(prevAns("cc")){
                if(a>=b && a>0){
                    ans+="a";
                    a--;
                }else if(b>=a && b>0){
                    ans+="b";
                    b--;
                }
            }else if(a>=b && a>=c && a>0){
                ans+="a";
                a--;
            }else if(b>=a && b>=c && b>0){
                ans+="b";
                b--;
            }else if(c>=a && c>=b && c>0){
                ans+="c";
                c--;
            }
            if(a==0 && b==0 && prevAns("cc")) break;
            if(b==0 && c==0 && prevAns("aa")) break;
            if(a==0 && c==0 && prevAns("bb")) break;
            if(a==0 && b==0 && c==0) break;
        }
        return ans;
    }
    boolean prevAns(String two) {
        int N = ans.length();
        if(N<2) return false;
        if(ans.charAt(N-2) == two.charAt(0) && ans.charAt(N-1) == two.charAt(1)) return true;
        return false;
    }
}//case 3: 2 2 1
