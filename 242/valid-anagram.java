class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length()!=t.length()) return false;
        int [] H1 = new int[26];
        int [] H2 = new int[26];
        for(int i=0; i<s.length(); i++){
            H1[s.charAt(i)-'a']++;
            H2[t.charAt(i)-'a']++;
        }
        for(int i=0; i<26; i++){
            if(H1[i]!=H2[i]) return false;
        }
        return true;
    }
}
