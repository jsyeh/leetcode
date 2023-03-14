class Solution {
public:
    string L1[27] = {"One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"};
    int L1N[27] = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,30,40,50,60,70,80,90};
    string twoDigit(int num) {
        string ans;
        for(int i=26; i>=0; i--){
            if(num>=L1N[i]){
                ans += " " + L1[i];
                num -= L1N[i];
            }
        }
        return ans.substr(1,ans.length()-1);
    }
    string threeDigit(int num) {
        string ans;
        if(num>=100){
            ans += " " + L1[num/100-1];
            ans += " Hundred";
            num = num % 100;
        }
        if(num>0) ans += " " + twoDigit(num);
        return ans.substr(1,ans.length()-1);
    }
    string Rank[3] = {
        "Thousand", "Million", "Billion"
    };
    int RankN[3] = {1000, 1000000, 1000000000};
    string numberToWords(int num) {
        if(num==0) return "Zero";
        string ans;
        int r=2;
        for(int r=2; r>=0; r--){
            if(num>=RankN[r]){
                int now = num / RankN[r];
                ans += " " + threeDigit(now);
                ans += " " + Rank[r];
                num = num % RankN[r];
            }
        }
        if(num>0) ans += " " + threeDigit(num);
        return ans.substr(1,ans.length()-1);
    }
};
