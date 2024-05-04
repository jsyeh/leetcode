// LeetCode 881. Boats to Save People
// people[i] 是某人體重，船有重量上限 limit，可裝1-2人，問要幾艘船，能載完全部人
// 關鍵應該是「重的人」先上船，再看剩下能再載哪個輕的人
// 所以 sort() 後，便能用簡單的 two pointers + greedy 來解
int cmp(const void *p1, const void *p2) {  // qsort() 需要自備 cmp() 比大小的函式
    return *(int*)p1 - *(int*)p2;
}
int numRescueBoats(int* people, int peopleSize, int limit) {
    qsort(people, peopleSize, sizeof(int), cmp);  // 利用 C 的 qsort() 排序
    int ans = 0;
    int left = 0, right = peopleSize - 1; // 左右邊界，以右邊「重的為主」處理
    while(left<=right) {  // 還有人還沒載走，就看看「若最重、最輕各挑1人」有否超重
        if(people[right] + people[left] <= limit) left += 1;
        right -= 1;  // 每趟一定可載走一個重的
        ans += 1;  // 每趟要多用一艘船
    }
    return ans;
} 

