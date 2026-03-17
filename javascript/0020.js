/*
    @param nums:{[Integer]}
    @return :{Boolean}
*/
function checkArithmeticSequence(nums){
    for (var i = 2; i < nums.length; i++) {
        if ((nums[i] - nums[i-1]) != (nums[i-1] - nums[i-2]))
            return false;
    }
    return true;
}
