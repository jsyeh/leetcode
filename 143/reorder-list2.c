//Linked List 分兩半，後半反過來，再交錯合起來。
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
void reorderList(struct ListNode* head) {
    struct ListNode* fast = head;
    struct ListNode* slow = head;
    while(fast->next!=NULL && fast->next->next!=NULL){
        fast = fast->next->next;
        slow = slow->next;
    } //利用 fast slow 找到中間位置(的前一格)
    struct ListNode* head2 = slow->next; //後半段的指標
    slow->next = NULL; //將前半段剪開
    struct ListNode* rev = NULL;
    while(head2!=NULL){ //要將後半段「反轉」
        struct ListNode* temp = head2->next;
        head2->next = rev;
        rev = head2;
        head2 = temp;
    }
    while(rev!=NULL){ //開始「交錯」
        struct ListNode* temp = head->next;
        head->next = rev;
        rev = temp; // head->next 和 rev 將兩個交換
        head = head->next; //head往下走
    }
}
