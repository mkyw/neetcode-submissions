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
    public bool IsValidBST(TreeNode root) {
        return ValidCheck(root, int.MaxValue, int.MinValue);
    }

    private bool ValidCheck(TreeNode curr, int max, int min) {
        if (curr == null) {
            return true;
        } else if (curr.val >= max || curr.val <= min) {
            return false;
        } else {
            return ValidCheck(curr.left, curr.val, min) &&
                ValidCheck(curr.right, max, curr.val);
        }
    }
}
