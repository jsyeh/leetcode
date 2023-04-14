class Solution {
    public int longestPalindromeSubseq(String s) {
        int N = s.length();
        char [] s1 = new char[N];
        char [] s2 = new char[N];
        for(int i=0; i<N; i++){
            s1[i] = s.charAt(i);
            s2[N-1-i] = s.charAt(i);
        }

        int [][] table = new int[N+1][N+1]; //table[i][j]表示 s1[i] s2[j] 最大common數量
        for(int i=0; i<=N; i++){
            table[0][0]=0;
            table[i][0]=0;
        }
        for(int i=1; i<=N; i++){
            for(int j=1; j<=N; j++){
                if(s1[i-1]==s2[j-1]) table[i][j] = table[i-1][j-1]+1;
                else table[i][j] = max(table[i-1][j], table[i][j-1]);
            }
        }
        return table[N][N];
    }
    int max(int a, int b){
        if(a>b) return a;
        else return b;
    }
}
