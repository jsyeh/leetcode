/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
// 對照 https://www.youtube.com/watch?v=pKO9UjSeLew 影片來理解
bool hasCycle(struct ListNode *head) {
    struct ListNode *fast = head; // 一開始是在頭的位置
    struct ListNode *slow = head; // 一開始是在頭的位置
    while(fast != NULL && fast->next != NULL){
        fast = fast->next->next; // 兩倍速跑
        slow = slow->next; // 一倍速跑
        if(fast==slow) return true; // 如果快的竟然會遇到慢的,表示「在繞圈圈」
    }
    return false; // 走完都沒有繞圈圈,就是沒有cycle
}
