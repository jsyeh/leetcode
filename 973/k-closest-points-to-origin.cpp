class Comp{
public:
    bool operator()( const vector<int> &a, const vector<int>&b ){
        return (a[0]*a[0]+a[1]*a[1]) < (b[0]*b[0]+b[1]*b[1]);
    }
};
class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        //priority_queue<int , vector<int>, greater<int>> pq;
        priority_queue<vector<int>, vector<vector<int>>, Comp> heap;

        for(vector<int> pt : points){
            heap.push(pt);
            if(heap.size()>k) heap.pop();
        }

        vector<vector<int>>ans;
        while(heap.size()>0){
            ans.push_back(heap.top());
            heap.pop();
        }

        return ans;
    }
};
