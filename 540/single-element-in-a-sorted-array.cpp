class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        int N = nums.size();
        if(N==1) return nums[0]; //針對 case 2/15: [1]

        int left = 0, right = N;
        while(left<right){
            int mid = (left+right)/2;
            if(mid%2==0 && nums[mid]==nums[mid+1]){ //正確成對
                left = mid + 1;
            }else if(mid%2==1 && nums[mid-1]==nums[mid]){ //也是正確成對
                left = mid + 1;
            }else{ //沒有成對
                right = mid;
            }
        }
        return nums[left];
    }
};
//case 2/15: [1]
