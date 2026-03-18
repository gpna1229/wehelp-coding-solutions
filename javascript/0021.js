/*
    @param nums:{[Integer]}
    @return :{Integer}
*/
function findMaxZero(nums){
    var flag = 0, maxZero = 0;
    for (var i = 0; i < nums.length; i++) {
        if (nums[i] == 0)
            maxZero = Math.max(maxZero, ++flag);
        else if (flag > 0) {
            maxZero = Math.max(maxZero, flag);
            flag = 0;
        } 
    }
    return maxZero;
}
