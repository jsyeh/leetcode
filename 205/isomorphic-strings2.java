class Solution {
    public boolean isIsomorphic(String s, String t) {
        char [] table1 = new char[256]; //s - t
        char [] table2 = new char[256]; //back t - s
        for(int i=0; i<s.length(); i++){
            char c1 = s.charAt(i), c2 = t.charAt(i);
            if(table1[c1]==c2 && table2[c2]==c1) continue;
            if(table1[c1]==0 && table2[c2]==0){
                table1[c1] = c2;
                table2[c2] = c1;
            } else return false;
        }
        return true;
    }
}
