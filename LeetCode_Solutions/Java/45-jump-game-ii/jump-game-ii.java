class Solution {
    public int jump(int[] nums) {
        int minJump = 0;
        int end = 0;
        int farthest = 0;

        // Start an implicit BFS.
        for (int i = 0; i < nums.length - 1; ++i) {
            farthest = Math.max(farthest, i + nums[i]);
                if (farthest >= nums.length - 1) {
                    ++minJump;
                    break;
                }
                if (i == end) {   // Visited all the items on the current level.
                    ++minJump;          // Increment the level.
                    end = farthest; // Make the queue size for the next level.
                }
        }

        return minJump;
    }
}