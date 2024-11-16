// LeetCode 134. Gas Station
// 加油站能加的油 gas[i] 及要花費的油 cost[i]
// 要順利「繞一圈」，問要從哪裡開始
class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int N = gas.size();
        int ansI = 0, totalGas = 0, nowGas = 0;
        for(int i=0; i<N; i++){ // 試著繞一圈
            totalGas += gas[i] - cost[i];
            nowGas += gas[i] - cost[i];
            if(nowGas<0){ // 如果油箱油不夠到下一站
                ansI = i+1; // 就換下一站出發
                nowGas = 0; // 油箱清空
            }
        }
        if(totalGas<0) return -1;
        return ansI;
    }
};
