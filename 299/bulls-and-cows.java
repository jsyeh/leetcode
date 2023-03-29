class Solution {
    public String getHint(String secret, String guess) {
        String ans = "";
        int [] H1 = new int[10];
        int [] H2 = new int[10];
        int A=0, B=0, N = secret.length();
        for(int i=0; i<N; i++) {
            if(secret.charAt(i)==guess.charAt(i)) A++;
            else{
                H1[secret.charAt(i)-'0']++;
                H2[guess.charAt(i)-'0']++;
            }
        }
        for(int i=0; i<10; i++){
            if(H1[i]<H2[i]) B += H1[i];
            else B += H2[i];
        }
        ans += "" + A + 'A' + B + 'B';
        return ans;
    }
}
