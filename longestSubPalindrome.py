def isPal(text):
    return text[0] == text[-1]

def longest_subpalindrome_slice(text):
    if(not text):
        return (0,0)
    text = text.lower()
    longestI = 0
    longestJ = 1
    i = 0.5
    bit = 0
    while(i<len(text)):
        if(not bit):
            startIndex = int(i-0.5)
            endIndex = int(i+1.5)
        else:
            startIndex = int(i-1)
            endIndex = int(i+2)

        if(startIndex<0 or endIndex>len(text)):
            i+=0.5
            bit = not bit
            continue
        else:
            t = text[startIndex:endIndex]
            while(isPal(t)):
                startIndex-=1
                endIndex+=1
                startIndex = int(startIndex)
                endIndex = int(endIndex)
                if(startIndex<0 or endIndex>len(text)):
                    break
                t = text[startIndex:endIndex]
            endIndex-=1
            startIndex+=1
            if (endIndex-startIndex) > (longestJ - longestI):
                longestJ = int(endIndex)
                longestI = int(startIndex)
        i+=0.5
        bit = not bit
    return (longestI,longestJ)


def test():
    L = longest_subpalindrome_slice
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    assert L('Race carr') == (7, 9)
    assert L('') == (0, 0)
    assert L('something rac e car going') == (8,21)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    assert L('abbacef') == (0,4)
    assert L('abba') == (0,4)
    return 'tests pass'

print test()



