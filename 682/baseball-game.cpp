class Solution {
public:
    int calPoints(vector<string>& operations) {
        vector<int> table;
        for(string op : operations){
            int N = table.size();
            if(op=="+"){
                int now = table[N-1] + table[N-2];
                table.push_back(now);
            }else if(op=="D"){
                int now = table[N-1];
                table.push_back(now*2);
            }else if(op=="C"){
                table.pop_back();
            }else{
                int now = stoi(op);
                table.push_back(now);
            }
        }
        int sum = 0;
        for(int n : table){
            sum += n;
        }
        return sum;
    }
};
