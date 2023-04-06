class Solution {
    public boolean checkInclusion(String s1, String s2) {
        int [] H1 = new int[26];//shoft
        int [] H2 = new int[26];//long

        for(int i=0; i<s1.length(); i++){
            H1[s1.charAt(i)-'a']++;
        }
/*        for(int i=0; i<s2.length(); i++){
            H2[s2.charAt(i)-'a']++;
        }
        for(int i=0; i<26; i++){
            if(H1[i]>H2[i]) return false;
        }
        return true;
        */
        int left=0, right=0;
        while(right<s2.length()) {
            //04:40先放棄,09:42重新回來,毛毛蟲前進法
            int c = s2.charAt(right) - 'a';
            //17:28迴圈TLE，可能有想錯
            while(H2[c]<=H1[c]){
//System.out.println(1);
                H2[c]++;
                right++;
                if(H2[c]>H1[c]) break;
                if(right-left==s1.length()) return true;
                if(right>=s2.length()) break;
                c = s2.charAt(right) - 'a';
            }
            while(H2[c]>H1[c]){
//System.out.println(2);
                int c2 = s2.charAt(left) - 'a';
                H2[c2]--;
                left++;
                if(left>=right)break;
            }
            if(right-left==s1.length()){
                return true;
            }
        }
        return false;
    }//02:30寫完，但測資有錯，需要思考，原來要substring
}
