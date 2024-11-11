// LeetCode 2601. Prime Subtraction Operation
class Solution {
public:
    int table[1001] = {}; // table[i]==0表示它是質數
    void buildTable() {
        for(int i=2; i<=1000; i++) {
            if(table[i]==0) {
                for(int k=i*i; k<=1000; k+=i) {
                    table[k] = 1; // killed
                }
            }
        }
    }
    int findPrimeBelow(int now) {
        for(int i=now-1; i>=2; i--) {
            if(table[i]==0) return i;
        }
        return 0;
    }
    bool primeSubOperation(vector<int>& nums) {
        if(table[4]==0) buildTable(); //還沒建table的話，建它
        nums[0] -= findPrimeBelow(nums[0]);
        for(int i=1; i<nums.size(); i++) {
            nums[i] -= findPrimeBelow(nums[i]-nums[i-1]);
            if(nums[i]<=nums[i-1]) return false;
        }
        return true;
    }
};
