class Freq {
public:
    int val;
    int count;
    Freq(int _val, int _count) {
        val = _val;
        count = _count;
    }
};
bool comp(const Freq& a, const Freq& b)
{
  return a.count < b.count;
}

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        vector<Freq> freq;
        int count=1;
        for(int i=0; i<nums.size(); i++){
            if(i==nums.size()-1 || nums[i]!=nums[i+1]) {
                Freq now(nums[i], count);
                freq.push_back(now);
                count=1;
            }else count++;
        }

        sort(freq.begin(), freq.end(), comp);
        vector<int> ans;
        for(int i=0; i<k; i++) {
            ans.push_back(freq[freq.size()-1-i].val);
        }

        return ans;
    }
};
