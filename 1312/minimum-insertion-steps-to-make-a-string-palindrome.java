class Solution {
    public int minInsertions(String s) {
        //idea： s 及 reverse s 的 editing distance(只加法)
        //後來看了 Discussion 真的有人提出來。與516. Longest Palindromic Subsequence相似，一試果然正確
        int ans=0;
        int N = s.length();
        char [] s1 = new char[N];
        char [] s2 = new char[N];
        for(int i=0; i<N; i++){
            s1[i] = s.charAt(i);
            s2[N-1-i] = s.charAt(i);
        }
        int [][] table = new int[N+1][N+1];
        // table[i][j] 表示 s1[i] s2[j] 最大相同的數量
        // 如果找到相同，那 N+N-相同，就是答案
        for(int i=0; i<=N; i++) {
            table[i][0] = 0;
            table[0][i] = 0;
        }

        for(int i=1; i<=N; i++){
            for(int j=1; j<=N; j++){
                if(s1[i-1]==s2[j-1]) table[i][j] = table[i-1][j-1] + 1;
                else {
                    table[i][j] = Math.max(table[i][j-1],table[i-1][j]);
                }
            }
        }
        return N-table[N][N];
    }
}
