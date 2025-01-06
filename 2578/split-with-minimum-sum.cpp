// LeetCode 2578. Split With Minimum Sum
// 把數字，分成2個數，希望數字「加起來」最小
class Solution {
public:
    int splitNum(int num) {
        vector<int> a;
        while(num>0){
            if(num%10>0) a.push_back(num%10); // 把非0項加入
            num /= 10;
        }
        sort(a.begin(), a.end()); // 小到大排序
        int ans = 0;
        if(a.size()%2==1) {
            ans = a[0]; // 奇數項，會多1位，先處理
            for(int i=1; i<a.size(); i+=2) { // 再平均分配
                ans = ans * 10 + a[i] + a[i+1];
            }
            return ans;
        } else { // 偶數項
            for(int i=0; i<a.size(); i+=2) { // 平均分配
                ans = ans * 10 + a[i] + a[i+1];
            }
            return ans;
        }
    }
};
