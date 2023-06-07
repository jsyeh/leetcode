class Solution {
public:
    int minFlips(int a, int b, int c) {
        int ans = 0;
        for(int i=0; i<31; i++){ //32個bit,只要算右邊31個bit
            int a2 = a%2, b2 = b%2, c2 = c%2; //剝皮，慢慢剝
    //printf("%d %d %d\n", a2, b2, c2); 我最喜歡 printf() debug了
            if((a2|b2)==c2){ 
                //合乎題目要求，沒事沒事
            }else if((a2|b2)==1 && c2==0){
                if(a2==1) ans++; //你要把1變0
                if(b2==1) ans++; //你要把1變0
            }else if((a2|b2)==0 && c2==1){
                ans++; //你要把隨便1個 0變1
            }

            a /= 2; //剝皮，變小囉
            b /= 2; //剝皮，變小囉
            c /= 2; //剝皮，變小囉
        }
        return ans;
    }
};
