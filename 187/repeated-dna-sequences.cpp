class Solution {
public:
    vector<string> findRepeatedDnaSequences(string s) {
        vector<string> ans;
        if(s.length()<10) return ans;
        unordered_set<string> set1; //有出現過
        unordered_set<string> set2; //已經 ans.push_back()
        for(int i=0; i<=s.length()-10; i++){
            string now = s.substr(i, 10);
            if(set1.find(now)!=set1.end()){ //有出現過
                if(set2.find(now)==set2.end()){ //還沒記錄
                    ans.push_back(now); //快記錄
                    set2.insert(now); //記錄了哦
                }
            }else set1.insert(now);
        }
        //最後1筆

        return ans;
    }
};
//case 2/31: "A"
//ase 25/31: "AAAAAAAAAAA"
