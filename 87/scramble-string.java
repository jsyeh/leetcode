class Solution {
    Map<String,Boolean> map = new HashMap<String,Boolean>();
    public boolean isScramble(String s1, String s2) {
        int N = s1.length();//保證兩個字串一樣長
        if(N!=s2.length())return false;
        if(s1.equals(s2)) return true;
        if(N==1) return false;

        if(map.containsKey(s1+" "+s2)) return map.get(s1+" "+s2);
        
        for(int i=1; i<N; i++){
            boolean noswap = isScramble(s1.substring(0,i), s2.substring(0,i))
                && isScramble(s1.substring(i), s2.substring(i));
            if(noswap){
                map.put(s1+" "+s2, true);
                return true;
            }

            boolean needswap = isScramble(s1.substring(0,i), s2.substring(N-i))
                && isScramble(s1.substring(i), s2.substring(0,N-i));
            if(needswap){
                map.put(s1+" "+s2, true);
                return true;
            }
        }
        map.put(s1+" "+s2, false);
        
        return false;
        /*int N = s1.length();
        boolean [][][]table = new boolean[N+1][N][N];
        for(int i=0; i<N; i++){
            for(int j=0; j<N; j++){
                table[1][i][j] = s1.charAt(i) == s2.charAt(i);
            }
        }

        //len越長，則i,j的範圍越小，所以 len是N時，i,j只剩下0
        for(int len=2; len<=N; len++){
            for(int i=0; i<N+1-len; i++){
                for(int j=0; j<N+1-len; j++){
                    for(int newLen=1; newLen<len; newLen++){
                        boolean same = table[newLen][i][j] && table[len-newLen][i+newLen][j+newLen];
                        boolean swap = table[newLen][i][j+len-newLen] && table[len-newLen][i+newLen][j];
                        table[len][i][j] |= same;
                        table[len][i][j] |= swap;
                    }
                }
            }
        }
        return table[N][0][0];*/
    }
}
