/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeElements(struct ListNode* head, int val) {
    struct ListNode* temp = (struct ListNode*)malloc(sizeof(struct ListNode)); // Create a new ListNode object 
    temp->next = head; // set the next node of temp to head
    struct ListNode *curr = temp; // create a new list node to track position
    while (curr->next != NULL) {
        if (curr->next->val == val) {
            curr->next = curr->next->next;
        } else {
        curr = curr->next;
        }
    }
    return temp->next;
}
