//決定誰是 winner, 好像可以用 Dynamic Programming來做
//每次可以從2端挑1個數字，最後誰挑得數字大，誰就是winner
//總共有20個數字，如果暴力法做，2^20 = 1024*1024全部的組合好像也不大
//不過最後我是使用 Editorial 的 Algorithm 1 的方法來解
int maxDiff(int* nums, int left, int right){
    if(left==right) return nums[left]; //拿到最後1個數字，diff值就是它

    int takeLeft = nums[left] - maxDiff(nums, left+1, right);
    int takeRight = nums[right] - maxDiff(nums, left, right-1);
    //前一筆的資料，要變負的，所以用 - maxDiff()

    return (takeLeft>takeRight)? takeLeft : takeRight;
}
bool PredictTheWinner(int* nums, int numsSize){
    int firstWinDiff = maxDiff(nums, 0, numsSize-1); //左右都包含

    if(firstWinDiff>=0) return true; //如果第一個人拿到的是比較多分 or 同分, win
    else return false; //第二個人 win
}
