class Solution {
    public int maxSubArray(int[] nums) {
        int Current_sum=nums[0];
		int Max_sum=nums[0];
		for(int i=1;i<nums.length;i++){
		    Current_sum=Math.max(nums[i],Current_sum+nums[i]);
		    Max_sum=Math.max(Max_sum,Current_sum);
		}
		return Max_sum;
        
    }
}