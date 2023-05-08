class Solution {
public:
    char nextGreatestLetter(vector<char>& letters, char target) {

        //陣列 letters[i]
        //for迴圈 for(int i=0; i<lettersSize; i++)
        //if判斷 if(letters[i]>target)
        //你完成了 90%, 但是有 一半的人會錯(有陷阱)

        //哨兵的技巧 sentinel 保護好你的程式,簡單,漂亮,不會錯
        char ans = 'z'+1; //字母國裡很大的數字,不合理的數字
        for(int i=0; i<letters.size(); i++){
            if(letters[i]>target && letters[i]<ans ){
            //要比 target大, 且  要比 ans小 (你要是最小的)
                ans = letters[i];
            }
        }

        if(ans=='z'+1) return letters[0];
        else return ans;        
    }
};
