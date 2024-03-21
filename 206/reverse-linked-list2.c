//這題用很多語言(C/C++/Java/Python)寫過很多次
// 這次想試試 C 的指標, 連接的方式, 是3個指標轉一圈。
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseList(struct ListNode* head){
    struct ListNode* ans = NULL; 
    while(head!=NULL){
        struct ListNode* next = head->next; //先備份(接下)下一筆的位置
        head->next = ans; //就可轉接(倒轉的重點)ans
        ans = head; //ans 可往左退一格
        head = next; //head 準備處理下一筆
    }
    return ans;
}
