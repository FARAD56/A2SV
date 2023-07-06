def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    sDict = {'(':1,')':2,'{':3,'}':4,'[':5,']':6}
    s.replace(' ','')
    if len(s) % 2 == 0:
        s = list(s)
        for i in range(1,len(s),2):
            if sDict[s[i]] - sDict[s[i-1]] == 1:
                continue
            else:
                return False
        return True

print(isValid())