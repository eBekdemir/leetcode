class Solution(object):
    def isValid(self, s):
        if len(s)%2 != 0: return False
        stack = []
        dct = {')':'(', '}':'{', ']':'['}
        for prt in s:
            if prt in dct.values():
                stack.append(prt)
            elif prt in dct:
                if len(stack)==0: return False
                last = stack.pop()
                if dct[prt] != last:
                    return False
        return True if len(stack) == 0 else False

