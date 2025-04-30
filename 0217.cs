using System.Linq;
public class Solution {
    public bool ContainsDuplicate(int[] nums) {
        var unique = nums.Distinct();
        if (unique.Count() < nums.Length) { return true; }
        return false;
    }
}


// second solution
public class Solution {
    public bool ContainsDuplicate(int[] nums){
        Dictionary<int, bool> numbers = new Dictionary<int, bool>(nums.Length);
        foreach (int i in nums){
            if (numbers.ContainsKey(i)){
                return true;
            }
            numbers.Add(i, true);
        }
        return false;
    }
}