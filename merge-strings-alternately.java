class Solution {
    public String mergeAlternately(String word1, String word2) {
        String ans = "";
        for(int i=0; i<word1.length() || i<word2.length(); i++){
            if(i<word1.length()) ans += word1.charAt(i);
            if(i<word2.length()) ans += word2.charAt(i);
        }
        return ans;
    }
}
