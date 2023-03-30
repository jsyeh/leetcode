class Solution {
    public boolean backspaceCompare(String s, String t) {
        char [] A = new char[s.length()];
        char [] B = new char[t.length()];

        int N1 = 0;
        for(int i=0; i<s.length(); i++){
            char c = s.charAt(i);
            if(c!='#'){
                A[N1] = c;
                N1++;
            } else {
                N1--;
                if(N1<0) N1=0;
            }
        }
        int N2 = 0;
        for(int i=0; i<t.length(); i++){
            char c = t.charAt(i);
            if(c!='#'){
                B[N2] = c;
                N2++;
            } else {
                N2--;
                if(N2<0) N2=0;
            }
        }
        if(N1!=N2) return false;
        for(int i=0; i<N1; i++){
            if(A[i]!=B[i]) return false;
        }
        return true;
    }
}
