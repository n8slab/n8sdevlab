class Solution {
    public List<String> summaryRanges(int[] nums) {
        List<String> solution = new ArrayList<>();

        for(int i=0; i<nums.length; i++){
            int start = nums[i];
            while (i+1 < nums.length && nums[i]==nums[i+1]-1){
                i++;
            }
            int end = nums[i];
            if(start == end){
                solution.add("" + start);
            } else {
                solution.add("" + start + "->" + end);
            }
        }

        return solution;
    }
}