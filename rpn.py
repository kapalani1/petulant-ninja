#python 3

import math

def isInt(s):
    try:
        val = int(s)
        return val
    except:
        return None
        
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for token in tokens:
            val = isInt(token)
            if(val is not None):
                stack.insert(0,val)
            else:
                val1 = stack.pop(0)
                val2 = stack.pop(0)
                if token == "+":
                    res = val1 + val2
                elif token == "-":
                    res = val2 - val1
                elif token == "*":
                    res = val1 * val2
                else:
                    b1 = val2 > 0
                    b2 = val1 > 0
                    if b1 ^ b2:
                        res = int(math.ceil(val2/val1))
                    else:
                        res = int(math.floor(val2 / val1))
                stack.insert(0, res)
        return stack.pop()   
