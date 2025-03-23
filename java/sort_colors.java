class Solution {
    private static void swap(int[] nums, int i1, int i2) {
        int temp = nums[i1];
        nums[i1] = nums[i2];
        nums[i2] = temp;
    }


    public void sortColors(int[] nums) {
        int zeroPointer = 0;
        int twoPointer = nums.length - 1;
        int i = 0;

        while(i <= twoPointer) {
            if(nums[i] == 2) {
                swap(nums, i, twoPointer);
                twoPointer--;
            }
            else if(nums[i] == 0) {
                swap(nums, i, zeroPointer);
                zeroPointer++;
                i++;
            }
            else {
                i++;
            }
        }
    }
}