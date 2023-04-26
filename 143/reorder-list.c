/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode * reverse(struct ListNode* head){
    struct ListNode ans;
    ans.next = NULL;
    struct ListNode *p = &ans;

    while(head!=NULL){
        struct ListNode * temp = p->next;
        p->next = head;
//printf("now: %d\n", head->val);
        head = head->next;
        p->next->next = temp;
        p = &ans;
    }
    
//    while(p!=NULL){
//        printf("->%d", p->val);
//        p = p->next;
//    }
    printf("\n");
    return ans.next;
}
void reorderList(struct ListNode* head){
    //這裡, 我照著解答的作法,先找到2段, 將後段 reverse, 再 merge
    if(head==NULL || head->next==NULL || head->next->next==NULL) return head; //簡單的先回傳
    struct ListNode * fast = head;
    struct ListNode * slow = head;
    while(fast->next!=NULL && fast->next->next!=NULL){
        fast = fast->next->next;
        slow = slow->next;
    }
//printf("mid: %d\n", slow->val);

    struct ListNode * part2 = reverse(slow->next);
    slow->next = NULL;
    struct ListNode * part1 = head;
    struct ListNode ans;
    struct ListNode *p = &ans;
    //merge head 及 part2
    while(part1!=NULL && part2!=NULL){
        p->next = part1;
        part1 = part1->next;
        p = p->next;

        p->next = part2;
        part2 = part2->next;
        p = p->next;
    }
    if(part1!=NULL){
        p->next = part1;
    }

    return ans.next;
}
