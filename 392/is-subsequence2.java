class Solution {
    public boolean isSubsequence(String s, String t) {
        if(s.length()==0 && t.length()==0) return true;
        if(s.length()>t.length()) return false;
        int k=0;
        for(int i=0; i<s.length(); i++){
            if(k<t.length() && s.charAt(i)==t.charAt(k)){
                k++;
            }else {
                while(k<t.length() && s.charAt(i)!=t.charAt(k)){
                    k++;
                }
                if(k==t.length()) return false;
                k++;
            }
        }
        return true;
    }
}
