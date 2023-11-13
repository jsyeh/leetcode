class Solution {
    public String addBinary(String a, String b) {
        String ans = ""; 
        int L1 = a.length(), L2 = b.length();
        int carry = 0;
        for(int i=0; i<L1 || i<L2; i++){
            int now = carry;
            if(i<L1) now += a.charAt(L1-i-1)-'0';
            if(i<L2) now += b.charAt(L2-i-1)-'0';
            carry = now / 2;
            ans += now%2;
        }
        if(carry>0) ans += 1;

        String ans2 = "";
        int L3 = ans.length();
        for(int i=0; i<L3; i++){
            ans2 += ans.charAt(L3-i-1);
        } // 使用 += 較無效率，之後可改 StrinBuilder 或 String.valueOf()
        // https://stackoverflow.com/questions/6952363/replace-a-character-at-a-specific-index-in-a-string
        return ans2;
    }
}
