class Solution {
public:
    //因為 N 最大是 10000, 所以 10^8 可能會超過時間, 不適拿暴力法
    //不過題目暗示暴力法有機會, 所以上傳看看
    vector<int> nextGreaterElements(vector<int>& nums) {
        int N = nums.size();
        vector<int> ans;
        for(int i=0; i<N; i++){
            int next = -1;
            for(int k=1; k<N; k++){
                if(nums[(i+k)%N] > nums[i]){
                    next = nums[(i+k)%N]; //要放值, 不是放index
                    break;
                }
            }
            ans.push_back(next);
        }
        return ans;
    }
};
//case 31/223: [5,4,3,2,1]
