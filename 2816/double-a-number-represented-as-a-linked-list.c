/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
// 這題用 Linked List 表示 10000 位大數，要模擬進位。
// 但這題更簡單：變成兩倍，自己加自己，本來就對齊。可省下反過來、反過去的步驟。
// 比較特別的地方，是「多1位」最高位。像 500+500=1000 要多1位
// 「四捨五入」概念： 500+500 會進位，499+499不會進位
struct ListNode* doubleIt(struct ListNode* head){
    if(head->val >= 5) {  // 如果「最高位」會進位，要多準備1位
        struct ListNode * temp = (struct ListNode*) malloc(sizeof(struct ListNode));
        temp->val = 0;  // 先準備好 memory，再將值放入
        temp->next = head;
        head = temp;  // 最後把 head 放最最高位
    }
    struct ListNode * now = head;
    while(now != NULL) {  // 還沒到 linked list 的最後
        now->val = (now->val * 2) % 10;  // 看這個位數，在變2倍後，會變多少
        if(now->next != NULL && now->next->val >= 5) {  // 下一位，有進位時
            now->val++;  // 答案就 +1
        }
        now = now->next;
    }
    return head;  // 直接使用 head 來放答案
}
