/*
    @param s:{String}
    @return :{Integer}
*/
function countWords(s){
    var countVoc = 0, flag = 1;
    for (var i = 0; i < s.length; i++) {
        if (s[i] == " ")
            flag = 1;
        else if (flag == 1)
            countVoc ++, flag = 0;
    }
    return countVoc;
}
