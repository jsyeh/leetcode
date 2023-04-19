class Solution {
    public String getHint(String secret, String guess) {
        int [] H1 = new int[10];
        int [] H2 = new int[10];
        int A=0, B=0;
        for(int i=0; i<secret.length(); i++){
            char c1=secret.charAt(i), c2=guess.charAt(i);
            if(c1==c2) A++;
            else{
                H1[c1-'0']++;
                H2[c2-'0']++;
            }
        }
        for(int i=0; i<10; i++){
            B += H1[i]<H2[i]?H1[i]:H2[i];
        }
        return A+"A"+B+"B";
    }
}
