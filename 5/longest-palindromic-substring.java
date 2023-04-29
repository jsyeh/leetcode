//照著 Editorial 方法3 Dynamic Programming 的概念實作
class Solution {
    public String longestPalindrome(String s) {
        int N = s.length();
        boolean [][] table = new boolean[N+1][N+1];

        for(int i=0; i<N; i++) table[i][i]=true;

        int max=1, maxI=0, maxlen=1;
        for(int i=0; i<N-1; i++) {
            if(s.charAt(i)==s.charAt(i+1)){
                table[i][i+1] = true;
                maxI = i;
                maxlen = 2;
//System.out.println("maxI:"+maxI + " maxlen:"+maxlen);
            }
        }
        for(int k=2; k<N; k++){
            for(int i=0; i<N-k; i++){
                if(table[i+1][i+k-1] && s.charAt(i)==s.charAt(i+k)) {
                    table[i][i+k] = true;
                    maxI = i;
                    maxlen = k+1;
//System.out.println("maxI:"+maxI + " maxlen:"+maxlen);
               }
            }
        }
        return s.substring(maxI, maxI+maxlen);
    }
}
