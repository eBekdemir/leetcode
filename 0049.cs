// URL: https://leetcode.com/problems/group-anagrams/                        
// TITLE: Group Anagrams                            
// DIFFICULTY: Medium                                
// ------------------------------------------------------
public class Solution {
    public IList<IList<string>> GroupAnagrams(string[] strs) {
        Dictionary<string, List<string>> theMap = new Dictionary<string, List<string>>();

        foreach (string s in strs) {
            char[] chars = s.ToCharArray();
            Array.Sort(chars);
            string sorted = new string(chars);

            if (theMap.ContainsKey(sorted)) {
                theMap[sorted].Add(s);
            } else {
                theMap[sorted] = new List<string> { s };
            }
        }

        return new List<IList<string>>(theMap.Values);
    }
}
