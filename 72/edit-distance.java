class Solution {
    public int minDistance(String word1, String word2) {
        int N1 = word1.length(), N2 = word2.length();
        int [][] distance = new int[N1+1][N2+1]; 
        //distance[i][j] 表示 word1 prefix i 到 word2 prefix j 的距離

        for(int i=0; i<=N1; i++) distance[i][0] = i;
        for(int j=0; j<=N2; j++) distance[0][j] = j;

        for(int i=1; i<=N1; i++){
            for(int j=1; j<=N2; j++){
                if(word1.charAt(i-1)==word2.charAt(j-1)) distance[i][j] = distance[i-1][j-1];
                else{
                    int d1 = distance[i-1][j] +1;
                    int d2 = distance[i][j-1] +1;
                    int d3 = distance[i-1][j-1] +1;
                    distance[i][j] = min(d1, d2, d3);
                }
            }
        }
        return distance[N1][N2];
    }
    int min(int a, int b, int c){
        if(a<=b && a<=c) return a;
        if(b<=a && b<=c) return b;
        if(c<=a && c<=b) return c;
        return c;
    }
}
