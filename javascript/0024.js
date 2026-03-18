/*
    @param sec:{Integer}
    @return :{[Integer]}
*/
function convertSeconds(sec){
    var arr = new Array(4);
    arr[3] = sec % 60;
    sec = Math.floor(sec / 60);
    arr[2] = sec % 60;
    sec = Math.floor(sec / 60);
    arr[1] = sec % 24;
    arr[0] = sec = Math.floor(sec / 24);
    return arr;
}
