class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        for(let i =0; i<nums.length-1; i++){
            for(let k =i+1;k<nums.length;k++){
                if(nums[i] == nums[i+1]){
                    return true
            }
                return false
            }
        }
    }
}
