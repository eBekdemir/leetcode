# URL: https://leetcode.com/problems/encode-and-decode-strings/                        
# TITLE: Encode and Decode Strings                            
# DIFFICULTY: Medium                                
# ------------------------------------------------------
class Solution:

    def encode(self, strs) -> str:
        return '#-#-#'.join(strs) if strs != [] else '#-None-#'
        
    def decode(self, s: str):
        spl = s.split('#-#-#')
        return spl if spl != ['#-None-#'] else []