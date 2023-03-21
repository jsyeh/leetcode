class Solution {
    public int strStr(String haystack, String needle) {
        int A = haystack.length(), B = needle.length();
        for(int i=0; i<A-B+1; i++){
            int bad=0;
            for(int k=0; k<B;k++){
                if(haystack.charAt(i+k)!=needle.charAt(k)) {
                    bad=1;
                    break;
                }
            }
            if(bad==0) return i;
        }
        return -1;
    }
}//Case 3: "a" "a"
// abc
// abc
