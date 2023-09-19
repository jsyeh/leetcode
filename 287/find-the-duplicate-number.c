// Joma If Programming Was An Anime 這個搞笑的影片，說明了解法
// https://www.youtube.com/watch?v=pKO9UjSeLew
// https://youtu.be/pKO9UjSeLew?si=eXw5j7cgdBmDYxCd&t=147
// 也就是重覆的數字，代表會到同一個index，這造成cycle發生
// 找到 cycle發生的位置，它的index就是答案
int findDuplicate(int* nums, int numsSize){
    int slow = nums[0], fast = nums[nums[0]];
    while(slow!=fast){
        slow = nums[slow];
        fast = nums[nums[fast]];
    }
    fast = 0;
    while(fast!=slow){
        fast = nums[fast];
        slow = nums[slow];
    }
    return slow;
}
