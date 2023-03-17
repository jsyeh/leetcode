class Solution {
    int [] H1 = new int[26];
    int [] H2 = new int[26];
    public boolean canConstruct(String ransomNote, String magazine) {
        for(int i=0; i<ransomNote.length(); i++){
            H1[ransomNote.charAt(i)-'a']++;
        }
        for(int i=0; i<magazine.length(); i++){
            H2[magazine.charAt(i)-'a']++;
        }
        for(int i=0; i<26; i++){
            if(H2[i]<H1[i]) return false;
        }
        return true;
    }
}
