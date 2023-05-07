class Solution {
public:
    int nearestValidPoint(int x, int y, vector<vector<int>>& points) {
        int min = INT_MAX, ans = -1;
        for(int i=0; i<points.size(); i++){
            int x2=points[i][0], y2=points[i][1];
            if(x2==x || y2==y){
                int dist2 = (x-x2)*(x-x2)+(y-y2)*(y-y2);
                if(dist2<min) {
                    min = dist2;
                    ans = i;
                }
            }
        }
        return ans;
    }
};
