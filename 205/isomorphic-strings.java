class Solution {
    char []tableST=new char[256];
    char []tableTS=new char[256];
    public boolean isIsomorphic(String s, String t) {
        int N = s.length();
        if(t.length()!=N) return false;

        for(int i=0; i<N; i++){
            char ss = s.charAt(i);
            char tt = t.charAt(i);
            if(tableST[ss]==0 && tableTS[tt]==0){
                tableST[ss]=tt;
                tableTS[tt]=ss;
            }else if(tableST[ss]==tt && tableTS[tt]==ss){
                continue;
            }else{
                return false;
            }
        }
        return true;
    }
}
//Case 4: s = "badc"
//t = "baba"
