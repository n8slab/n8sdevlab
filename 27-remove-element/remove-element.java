import java.lang.Object;
class Solution {
    public int removeElement(int[] nums, int val) {
        //skip null case exception
        if (nums == null || nums.length == 0) {
            return 0;
        }

        //set pointers
        int len = nums.length;
        int j = len - 1;

        //start counter for number of val occurences
        int k = 0;

        for (int i = 0; i < len; i++) {
            if (nums[i] == val) {
                //increment counter
                k++;
                //close loop if thats the last index
                if (j == i) {
                    return len - k;
                }
                //check if last element is equal to the val to be removed, then work backwards
                while (nums[j] == val) {
                    //update the end pointer to the next value to be checked. Update occurence pointer
                    j--;
                    k++;
                    //end loop if we're done searching all the indexes
                    if (j == i) {
                        return len - k;
                    }
                }
                //swap the pointers before loop repeats
                nums[i] = nums[j];
                j--;
            }
            if (i == j) {
                return len - k;
            }
        }
        return len - k;
    }
}