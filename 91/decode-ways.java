class Solution {
    public int numDecodings(String s) {
        table = new int[s.length()];
        return numDecodings(s, 0);
    }
    int [] table;
    int numDecodings(String s, int i) {
        if(i>=s.length()) return 1;
        if(s.charAt(i)=='0') {//invalid
            table[i] = 0;
            return 0;
        }
        if(s.charAt(i)!='0' && i==s.length()-1) return 1;
        if(table[i]!=0) return table[i];

        int ans = 0;
        ans += numDecodings(s, i+1);
        if(s.charAt(i)<='1') ans += numDecodings(s, i+2);
        else if(s.charAt(i)=='2' && i<s.length()-1 && s.charAt(i+1)<='6') ans += numDecodings(s, i+2);

        table[i] = ans;
        return ans;
    }
}
