/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseList(struct ListNode* head){
    //簡單的，直接結束
    if(head==NULL || head->next==NULL) return head;

    //拆成 head 及 head.next, 再把 head.next都倒轉好
    struct ListNode* ans = reverseList(head->next); 
    //倒轉後，ans的最後一筆，是 head.next, 要接回（拆開的）head
    head->next->next = head; //接回 head
    head->next = NULL; //接地
    return ans;
}
