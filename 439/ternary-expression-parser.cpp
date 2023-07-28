//這題想到要用 stack 的資料結構。函式呼叫函式 也是 stack 相關
//最後是參考 Editorial Approach5: Recursion 因為和原本想法很像，容易理解
class Solution {
public:
    string parseTernary(string str) {
        return parse(str, 0, str.length()-1); //左右包含 
    }

    string parse(string str, int left, int right) { //左右包含
//cout << "str.substr(left, 1) is " << str.substr(left, 1) << endl;
        if(left==right) return str.substr(left, 1); //將會是 "T" 或 "F"

        int op1 = str.find("?", left+1); //op1: 問號所在位置
        int op2 = op1+1, q=1; //op2: 冒號所在位置
        for(int i=op1+1; i<=right; i++){
            if(str[i]=='?') q++; //如果有多的問號，那就要再多找冒號才行
            else if(str[i]==':'){
                q--; //利用 q 這個變數，來確認 op1 問號 對應的 op2 冒號，有對應
                if(q==0){ //配對數量剛剛好
                    op2 = i; //更新 op2 的位置
                    break;
                }
            }
        }
//cout << str[left] << " " << op1 << " " << op2 << " " << right << endl;
        if(str[left]=='T') return parse(str, op1+1, op2-1); //問號右邊、冒號左邊
        else return parse(str, op2+1, right); //冒號右邊、結尾的右邊界
    }
};
