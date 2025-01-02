// LeetCode 1427. Perform String Shifts
// 字串 s ，請照 shift[i] 裡，會有「運行方向」（0向左、1向右）及「移動量」改變字串
class Solution {
public:
    string stringShift(string s, vector<vector<int>>& shift) {
        int head = 0;
        for(int i=0; i<shift.size(); i++) {
            int d = shift[i][0], a = shift[i][1];
            if(d==0) head += a;
            else head -= a;
        }
        int N = s.length();
        head = (head % N + N) % N;
        string ans = s.substr(head, N-head) + s.substr(0, head);
        return ans;
    }
};
