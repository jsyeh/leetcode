class Solution {
public:
    int strStr(string haystack, string needle) {
        int N1 = haystack.length(), N2 = needle.length();
        if(N2>N1) return -1;

        for(int i=0; i<N1-N2+1; i++){
            int bad = 0;
            for(int j=0; j<N2; j++){
                if(haystack[i+j]!=needle[j]){
                    bad = 1;
                    break;
                }
            }
            if(bad==0) return i;
        }
        return -1;
    }
};
//case 70/79: "a" "a"
