class Solution {
    public boolean isSubsequence(String s, String t) {
        int ti=0;
        for(int si=0; si<s.length(); si++){
            char sc=s.charAt(si);
            while(ti<t.length()){
                char tc=t.charAt(ti);
                if(sc==tc) break;
                ti++;
            }
            if(si==s.length()-1 && ti==t.length()-1) return true;
            if(ti==t.length()) return false;

            ti++;
        }
        return true;
    }
}
