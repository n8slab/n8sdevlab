class Solution {
    public boolean canJump(int[] nums) {
        boolean atEnd = false;
        int atStep = 0;

        for(int i=0; atStep<nums.length && atStep<=i; ++atStep){
            i = Math.max(i, atStep + nums[atStep]);
        }

        atEnd = atStep==nums.length;
        return atEnd;
    }
}