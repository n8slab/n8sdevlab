class Solution {
    public int removeDuplicates(int[] nums) {
            if (nums.length == 0) return 0;
    int j = 0;
    int count = 1;
    for (int i = 1; i < nums.length; i++) {
      if (nums[i - 1] == nums[i]) {
        count++;
      } else {
        count = 1;
      }
      if (count == 1 || count == 2) {
        j++;
        nums[j] = nums[i];
      }
    }
    return j + 1;
    }
}