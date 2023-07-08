//好像可以用昨天用到的方法，拉著框框前進
int lengthOfLongestSubstringKDistinct(char * s, int k){
    int N = strlen(s);
    int ascii[256] = {}; //都設為0
    int left = 0, right = 0, kd = k; //kd: 功德值
    for(int i=0; i<N; i++){
        char c = s[i];
        if(ascii[c]==0){ //有1個新的字母出現了
            ascii[c]++;
            kd--; //用掉1個功德值
            if(kd>=0){ //功德值足夠，還可以增長
                right++;
            }else{ //功德值不足，只好吐出
                char c2 = s[left];
                ascii[c2]--;
                if(ascii[c2]==0) kd++;//又恢復一個功德值
                right++;
                left++;
            }
        }else{ //沒有增加新的字母
            ascii[c]++; //加的是舊的字母
            if(kd>=0){
                right++;
            }else{
                char c2 = s[left];
                ascii[c2]--;
                if(ascii[c2]==0) kd++;
                right++;
                left++;
            }
        }
    }
    return right - left;
}
