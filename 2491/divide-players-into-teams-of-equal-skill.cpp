// LeetCode 2491. Divide Players Into Teams of Equal Skill
// 將N個數字，2個一組，分成 N/2 個團隊，每個團隊有均衡skill組合（加起來相同）。
class Solution {
public:
    long long dividePlayers(vector<int>& skill) {
        sort(skill.begin(), skill.end()); // 從小到大排好
        int N = skill.size(); // 總人數
        // 要小心「int只有32位元」可能不夠加，所以要用 long long int
        long long int total = accumulate(skill.begin(), skill.end(), 0); // 總點數
        if(total % (N/2) != 0) return -1; // 無法整除，就無法順利「平均分配」skill點數
        long long int average = total / (N/2);  // 「平均分配」skill點數
        long long int ans = 0; // 最後加總的答案
        for(int i=0; i<N/2; i++){
            // 但是 C/C++ 遇到「兩個很大的
            if(skill[i]+skill[N-1-i] != average) // 左邊最小 + 右邊最大，不是團隊「平均分配」skill點數
                return -1; // 就失敗了
            ans += skill[i] * skill[N-1-i]; // 兩兩相乘，再加起來
        }
        return ans;
    }
};
