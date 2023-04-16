class Solution {
    public int numWays(String[] words, String target) {
        int len = words[0].length(), len2 = target.length();
        char [][] H = new char[len][26];
        for(String word : words){
            for(int i=0; i<len; i++){ //第[i]格[某個字母]出現次數
                H[i][word.charAt(i)-'a']++;
            }
        }

        long [][] table = new long[len+1][len2+1];//table[len][len2] 用前len對應target前len2
        for(int i=0; i<=len; i++) table[i][0] = 1;

        for(int i=1; i<=len; i++){ //有移1格
            for(int j=1; j<=len2 && j<=i; j++){ //有移1格
                char c = target.charAt(j-1);
                table[i][j] = mod(table[i-1][j-1] * H[i-1][c-'a'] + table[i-1][j]);
            }
        }
        return (int)table[len][len2];
    }
    long mod(long n) {
        return n%1000_000_007;
    }
}
