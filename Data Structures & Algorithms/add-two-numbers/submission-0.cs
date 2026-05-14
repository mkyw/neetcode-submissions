/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

public class Solution {
    public ListNode AddTwoNumbers(ListNode l1, ListNode l2) {
        ListNode ans = new ListNode();
        ListNode curr = ans;
        int carry = 0;
        int sum = 0;
        while (l1 != null || l2 != null) {
            if (l1 == null) {
                sum = l2.val + carry;
                l2 = l2.next;
            } else if (l2 == null) {
                sum = l1.val + carry;
                l1 = l1.next;
            } else {
                sum = l1.val + l2.val + carry;
                l1 = l1.next;
                l2 = l2.next;
            }
            curr.next = new ListNode();
            curr.next.val = sum % 10;
            carry = sum / 10;

            curr = curr.next;
        }
        if (carry != 0) {
            curr.next = new ListNode();
            curr.next.val = carry;
        }
        return ans.next;
    }
}
