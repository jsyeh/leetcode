class Solution {
    public boolean repeatedSubstringPattern(String s) {
        int N = s.length();
        String s2 = (s+s).substring(1,N*2-1);
//System.out.println(s2);
        return s2.indexOf(s)!=-1;
    }
}
