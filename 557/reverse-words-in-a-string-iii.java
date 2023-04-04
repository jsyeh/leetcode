class Solution {
    public String reverseWords(String s) {
        String ans = "";
        int begin=0, end=0;
        for(int i=0; i<=s.length(); i++) {
            if(i == s.length() || s.charAt(i)==' '){
                end = i;
                for(int k=end-begin-1; k>=0; k--){
                    ans += s.charAt(begin+k);
                }
                if(i<s.length() && s.charAt(i)==' ')ans += ' ';
                begin=i+1;
            }
        }
        return ans;
    }
}
