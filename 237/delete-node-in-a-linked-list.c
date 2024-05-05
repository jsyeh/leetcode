/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
// 今天 LeetCode 挑戰題，可以說很難
//（Median中等題，要用到大二資料結構的Linked List觀念，又需要拐個奇怪的彎），
// 也可以說很簡單（程式碼只需要2行）。
// 題目是給你一個指標，指到一個 node 資料結構。然後想把它刪掉。
// 但是，你又不能「真的把它刪掉」，因為你「只有這個node」及之後的nodes的資訊，
// 而沒有「前一個node」的資訊，所以真的無法「刪不掉它」。
// 解法：拐個彎，不需要把它刪掉，而是把它「打扮成下一個node」，
//      再把「下一個node犧牲忽略掉」就完成了。
void deleteNode(struct ListNode* node) {
    // 題目保證不是最後一點，所以「存在node->next」
    node->val = node->next->val;  // 把下一筆的「值」往前移
    node->next = node->next->next;  // 把下一筆的「指標」往前移    
}
