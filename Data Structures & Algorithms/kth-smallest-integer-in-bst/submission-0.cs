/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

public class Solution {
    public int KthSmallest(TreeNode root, int k) {
        Stack<TreeNode> stack = new Stack<TreeNode>();
        TreeNode curr = root;
        int count = 0;
        while (curr != null || stack != null) {
            if (curr != null) {
                stack.Push(curr);
                curr = curr.left;
            } else {
                curr = stack.Pop();
                count += 1;
                if (count == k) {
                    return curr.val;
                }
                curr = curr.right;
            }
        }
        return -1;
    }
}
