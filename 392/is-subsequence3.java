class Solution {
    public boolean isSubsequence(String s, String t) {
        int i=0, k=0;
        while(i<s.length() && k<t.length()){
            char c = s.charAt(i);
            char c2 = t.charAt(k);
            if(c==c2){
                i++;
                k++;
            }else{
                k++;
            }
        }
        if(i==s.length()) return true;
        else return false;
    }
}
