// LeetCode 881. Boats to Save People
// people[i] 是某人體重，船有重量上限 limit，可裝1-2人，問要幾艘船，能載完全部人
// 關鍵應該是「重的人」先上船，再看剩下能再載哪個輕的人
// 所以 sort() 後，便能用簡單的 two pointers + greedy 來解
class Solution { // 因為 C++ 可以簡單使用 sort() 所以用 C++ 試試
public:
    int numRescueBoats(vector<int>& people, int limit) {
        sort(people.begin(), people.end());  // 利用 C++ 的 sort()
        int ans = 0;
        int left = 0, right = people.size() - 1;  // 左右邊界，以右邊「重的為主」處理
        while(left<=right) {  // 還有人還沒載走，就看看「若最重、最輕各挑1人」有否超重
            if(people[right] + people[left] <= limit) left += 1;
            right -= 1;  // 每趟一定可載走一個重的
            ans += 1;  // 每趟要多用一艘船
        }
        return ans;
    }
};

