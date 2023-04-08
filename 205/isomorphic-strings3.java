class Solution {
    public boolean isIsomorphic(String s, String t) {
        if(s.length()!=t.length()) return false;

        char [] table = new char[256];
        char [] table2 = new char[256];
        for(int i=0; i<s.length(); i++){
            char c = s.charAt(i);
            char c2 = t.charAt(i);
            if(table[c]==0 && table2[c2]==0){
                table[c]=c2;
                table2[c2]=c;
            }else if(table[c]!=c2 || table2[c2]!=c){
                return false;
            }
        }
        return true;
    }
}//Case 4: s = "badc"
//t = "baba"
