public class Solution {
    public bool hasDuplicate(int[] nums) {
        HashSet<int> seen = new HashSet<int>();
        for (int i = 0; i < nums.Length; i+=1) {
            if (seen.Contains(nums[i])) {
                return true;
            }
            seen.Add(nums[i]);
        }
        return false;
    }
}