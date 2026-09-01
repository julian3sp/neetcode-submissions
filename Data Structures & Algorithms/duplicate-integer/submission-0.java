class Solution {
    public boolean hasDuplicate(int[] nums) {
 Stack<Integer> s = new Stack<>();
 for(int i : nums){
    if(s.contains(i)){
        return true;
    } else {
        s.push(i);
    }
 }
 return false;
    }
}
