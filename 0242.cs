// URL: https://leetcode.com/problems/valid-anagram/                        
// TITLE: Valid Anagram                            
// DIFFICULTY: Easy                                
// ------------------------------------------------------
public class Solution {
    public bool IsAnagram(string s, string t) {
        if (s.Length != t.Length){ return false; }
        Dictionary<char, int> dict = new Dictionary<char, int>();
        foreach (char i in s){
            if (dict.ContainsKey(i)){
                dict[i] += 1;
            }
            else {
                dict.Add(i, 1);
            }
        }
        foreach (char i in t){
            if (dict.ContainsKey(i)){
                if (dict[i] == 0) {return false;}
                dict[i] -= 1;
            }
            else {
                return false;
            }
        }
        return true;
    }
}