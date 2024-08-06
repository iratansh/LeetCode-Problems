public class Solution {
    public int MajorityElement(int[] nums) {
        Dictionary<int, int> elements_count = new Dictionary<int, int>();
        for (int i = 0; i < nums.Length; i++) {
            if (elements_count.ContainsKey(nums[i])) {
                continue;
            } else {
                elements_count.Add(nums[i], 0);
            }
        }
        for (int i = 0; i < nums.Length; i++) {
            elements_count[nums[i]] += 1;
        }
        return elements_count.MaxBy(entry => entry.Value).Key;
    }
}
