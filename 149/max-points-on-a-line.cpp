// LeetCode 149. Max Points on a Line
// 一堆點，最多有「幾點」共線。
class Solution {
public:
    int maxPoints(vector<vector<int>>& points) {
        int ans = 0; // 相同斜率的線，有幾條
        for (int i=0; i<points.size(); i++) { // 每次挑一個點當基準
            map<float,int> m; // m[斜率slope] 對應 斜率slope 的線段數量
            float x = points[i][0], y = points[i][1], slope;
            for (int k=0; k<points.size(); k++) {
                if (k==i) continue; // 相同的點，不計入
                if(points[k][0]-x==0) slope = FLT_MAX; // 斜率「無限大」
                else slope = (points[k][1]-y) / (points[k][0]-x); //正常斜率
                m[slope]++; // 此斜率的線段 +1
                ans = max(ans, m[slope]); // 更新答案
            }
        }
        return ans+1; // 共線的點，是(以某點當基準點)共線的線「數量」+1
    }
};
