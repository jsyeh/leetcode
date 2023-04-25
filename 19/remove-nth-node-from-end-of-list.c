/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeNthFromEnd(struct ListNode* head, int n){
  struct ListNode * ans = head;
  int len =0;
  while(head!=NULL){
    head = head->next;
    len++;
  }
  //printf("%d\n", len);
  if(len==n) return ans->next;
  head = ans;
  for(int i=0; i<len-n-1; i++){
    head = head->next;
  }
  head->next = head->next->next;
  return ans;
}//case [1,2] 2
