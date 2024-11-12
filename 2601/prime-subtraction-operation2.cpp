// LeetCode 2601. Prime Subtraction Operation
class Solution {
public:
    vector<int> prime;
    void buildPrime() {
        int table[1001] = {};
        for(int i=2; i<=1000; i++) {
            if(table[i]==0){
                prime.push_back(i);
                for(int k=i*i; k<=1000; k+=i) table[k] = 1;
            }
        }
    }
    int findPrimeBelow(int now) {
        auto pos = upper_bound(prime.begin(), prime.end(), now-1);
        if(pos==prime.begin()) return 0;
        return prime[pos-prime.begin()-1];
    }
    bool primeSubOperation(vector<int>& nums) {
        if(prime.size()==0) buildPrime(); // 第1次使用時，建立 prime 陣列
        nums[0] -= findPrimeBelow(nums[0]);
        for(int i=1; i<nums.size(); i++) {
            nums[i] -= findPrimeBelow(nums[i]-nums[i-1]);
            if(nums[i]<=nums[i-1]) return false;
        }
        return true;
    }
};
