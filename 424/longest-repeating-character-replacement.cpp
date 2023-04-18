class Solution {
public:
    int characterReplacement(string s, int k) {
        int H[26]={};
        int left=0, right=0, max=1;
        while(right<s.length()) {
            H[s[right++]-'A']++;
            int now = checkMaxRepeat(H, k);
            while(now==-1 && left<right){ //不合格,就變短一些
                H[s[left++]-'A']--;
                now = checkMaxRepeat(H, k);
            }
printf("%d %d\n", left, right);
            if(now>max){
                max=now;
            }
        }
        return max;
    }
    int checkMaxRepeat(int H[26], int k){
        int max=0, sum=0;
        for(int i=0; i<26; i++){
            if(H[i]>max) max=H[i];
            sum+=H[i];
        }
        if(sum-max<=k) return sum;//合格,因noise<=k, 全部都可Repeat的值
        else return -1; //不合格的意思,noise太多
    }
};
//case3: "ABAA" 3 在離開迴圈時,應再做一次檢查
