class Solution {
public:
    vector<bool> checkArithmeticSubarrays(vector<int>& nums, vector<int>& l, vector<int>& r) {
        //題目的意思, 是 query: l[i] ... r[i] 對應的 nums[l] ... nums[r] 是等差數量
        //所以就暴力試看看吧
        vector<bool> ans;
        for(int i=0; i<l.size(); i++) {
            int a = l[i], b = r[i];
            vector<int> list;
            for(int k=a; k<=b; k++){
                list.push_back(nums[k]);
            }
            sort(list.begin(), list.end());
            int bad = 0;
            for(int k=1; k<list.size(); k++){
                if(list[k]-list[k-1] != list[1]-list[0]) bad = 1;
            }
            if(bad==0) ans.push_back(true);
            else ans.push_back(false);
        }
        return ans;
    }
};
