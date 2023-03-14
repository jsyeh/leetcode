class Solution {
public:
    string Symbol[21] = {
        "I", "I", "I", "IV", "V", "IX", 
        "X", "X", "X", "XL", "L", "XC",
        "C", "C", "C", "CD", "D", "CM",
        "M", "M", "M"};
    int Value[21] = {
        1, 1, 1, 4, 5, 9,
        10,10,10,40,50,90,
        100,100,100,400,500,900,
        1000, 1000, 1000};
    string intToRoman(int num) {
        string ans;
        for(int i=20; i>=0; i--){
            if(num>=Value[i]){
                ans+=Symbol[i];
                num-=Value[i];
            }
        }
        return ans;
        
    }
/*    char Symbol[7] = {'I', 'V', 'X', 'L', 'C', 'D', 'M'};
    int Value[7] = {1, 5, 10, 50, 100, 500, 1000};
    string intToRoman(int num) {
        int index=6;
        string ans;
        while(num>0){
            while(num>=Value[index]){
                ans += Symbol[index];
                num -= Value[index];
            }
            index--;
        }
        return ans;
    }*/
};
