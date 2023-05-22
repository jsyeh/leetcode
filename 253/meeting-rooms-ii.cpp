class Time {
public:
    int t;
    int end; //0: begin, 1: end
    Time(int _t, int _end) {
        t = _t;
        end = _end;
    }
};
bool comp(const Time& a, const Time& b) {
    if(a.t!=b.t) return a.t < b.t;
    return a.end > b.end;
}
//bool comp(const vector<int>&a, const vector<int>&b) {
//    return a[1] < b[1];
//}

class Solution {
public:
    int minMeetingRooms(vector<vector<int>>& intervals) {
        //sort(intervals.begin(), intervals.end(), comp);
        //for(int i=0; i<intervals.size(); i++){
        //    printf("%d %d\n", intervals[i][0], intervals[i][1]);
        //}

        vector<Time> details;
        for(int i=0; i<intervals.size(); i++){
            Time t0(intervals[i][0], 0);
            Time t1(intervals[i][1], 1);
            details.push_back(t0);
            details.push_back(t1);
        }
        sort(details.begin(), details.end(), comp);
        int ans = 0, rooms = 0;
        for(int i=0; i<details.size(); i++){
            //printf("%d %d\n", detail[i].t, detail[i].end);
            if(details[i].end==0) rooms++;
            else if(details[i].end==1) rooms--;
            if(rooms>ans) ans = rooms;
        }

        return ans;
    }
};
