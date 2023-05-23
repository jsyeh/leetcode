class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int N = temperatures.size();

        vector<int> ans(N);
        stack<int> s; //s.top() 裡面放的,是前一個沒得到解答的人

        for(int i=0; i<N; i++) {
            while( s.size()>0 && temperatures[s.top()] < temperatures[i] ) {
                //天氣相對比較熱沒錯, 把s.pop() 吧
                ans[s.top()] = i-s.top();
                s.pop();
            }
            s.push(i);//如果無法判斷, 就先丟到stack裡, 等之後再解開
        }
        return ans;
    }
};
