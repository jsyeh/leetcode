class Solution {
    public int compress(char[] chars) {
        if(chars.length==0) return 0;
        char prev = chars[0];
        int N = 1;
        int k=1;
        for(int i=1; i<chars.length; i++){
            if(chars[i]==prev){
                N++;
            }
            if(chars[i]!=prev){
                k += myPut(chars, k, N);//把N的值塞到chars裡
                prev = chars[i];
                chars[k] = chars[i];
                k++;
                N=1;
            }
            if(i==chars.length-1) {
                k += myPut(chars, k, N);
            }
        }
        return k;
    }
    int myPut(char[] chars, int k, int N) {
        if(N==1) return 0;
        String s = "" + N;
        for(int i=0; i<s.length(); i++) {
            chars[k+i] = s.charAt(i);
        }
        return s.length();
    }
}//case4: ["a","a","a","b","b","a","a"]
