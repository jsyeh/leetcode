class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        int M = text1.length(), N = text2.length();
        int table[M+1][N+1];
        for(int i=0; i<M+1; i++) table[i][0] = 0;
        for(int j=0; j<N+1; j++) table[0][j] = 0;

        for(int i=1; i<M+1; i++){
            for(int j=1; j<N+1; j++){
                if(text1[i-1]==text2[j-1]){
                    table[i][j] = table[i-1][j-1] + 1;
                    if(table[i-1][j]>table[i][j]) table[i][j] = table[i-1][j];
                    if(table[i][j-1]>table[i][j]) table[i][j] = table[i][j-1];
                }else{
                    table[i][j] = table[i-1][j];
                    if(table[i][j-1]>table[i][j]) table[i][j] = table[i][j-1];
                }
            }
        }

        return table[M][N];
    }
};
