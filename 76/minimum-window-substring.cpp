class Solution {
public:
    string minWindow(string s, string t) {
        int H[52]={};
        int HT[52]={};
        for(int i=0; i<t.length(); i++){
            char c = t[i];
            if(c>='A' && c<='Z') HT[c-'A']++;
            else if(c>='a' && c<='z') HT[c-'a'+26]++;
        }

        int min_len = INT_MAX, minI = 0;
        int left = 0;
        for(int i=0; i<s.length(); i++){
            char c = s[i], k;
            if(c>='A' && c<='Z') k = c - 'A';
            else if(c>='a' && c<='z') k = c-'a'+26;
            H[k]++;
            if(H[k]<HT[k]) continue; //還不夠，就繼續走

            int bad=0;
            for(int i=0; i<52; i++){
                if(H[i]<HT[i]){
                    bad=1;
                    break;
                }
            }
            if(bad==1) continue; //還不夠，繼續走
            else{ //是合理的
                //要縮短,將left右移
                while(true){
                    char c = s[left];
                    if(c>='A' && c<='Z') c = c - 'A';
                    else c = c - 'a' + 26;
                    if(H[c]-1>=HT[c]){
                        H[c]--;
                        left++;
                        continue;
                    }
                    break;
                }
                if(i-left+1<min_len){
                    min_len = i-left+1;
                    minI = left;
                }
            }
            //printf("left:%d i:%d minI:%d min_len:%d\n", left, i, minI, min_len);
        }
        if(min_len==INT_MAX) return "";
        else return s.substr(minI, min_len);
    }
};
