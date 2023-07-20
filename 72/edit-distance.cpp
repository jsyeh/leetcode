class Solution {
public:
    int minDistance(string word1, string word2) {
        int N1 = word1.length(), N2 = word2.length();
        int table[N1+1][N2+1];
        for(int i=0; i<=N1; i++) table[i][0] = i; //"" 走到 word1[i] 距離是i
        for(int j=0; j<=N2; j++) table[0][j] = j; //"" 走到 word2[j] 距離是j

        for(int i=1; i<=N1; i++) {
            for(int j=1; j<=N2; j++) {
                if(word1[i-1]==word2[j-1]) {
                    table[i][j] = table[i-1][j-1]; //相同不用編輯，edit距離沒增加
                } else {
                    int d1 = table[i-1][j-1] + 1; //修改取代1個字母
                    int d2 = table[i-1][j] + 1; //刪除1個字母
                    int d3 = table[i][j-1] + 1; //增加1個字母
                    table[i][j] = min(d1,d2,d3);
                }
            }
        }
        return table[N1][N2];
    }
    int min(int a, int b, int c) {
        if(a<=b && a<=c) return a;
        if(b<=a && b<=c) return b;
        return c;
    }
};
