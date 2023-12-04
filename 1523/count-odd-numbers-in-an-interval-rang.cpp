// 這題不能用for迴圈慢慢算，因為數字會很大
// 所以就直接數字相減就好了
// 奇-奇：1 3 5 7 9 = (9-1)//2 + 1
// 偶-奇：0 1 3 5 7 = (7-0)//2 + 1
// 奇-偶：1 3 5 6 = (6-1)//2 + 1
// 偶-偶：0 1 3 5 6 = (6-0)//2
class Solution {
public:
    int countOdds(int low, int high) {
        //if(low%2==1 && high%2==1) return (high-low)/2 + 1;
        //if(low%2==0 && high%2==1) return (high-low)/2 + 1;
        //if(low%2==1 && high%2==0) return (high-low)/2 + 1;
        //if(low%2==0 && high%2==0) return (high-low)/2;
        if(low%2==0 && high%2==0) return (high-low)/2;
        else return (high-low)/2 + 1;
    }
};
