class Solution:
    def romanToInt(self, s: str) -> int:
        dic =  {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        length = len(s)
        i=0
        summ = 0

        while i<length:
            if i<length-1 and dic[s[i]] < dic[s[i+1]]:
                summ += dic[s[i+1]] - dic[s[i]]
                i += 2
            else:
                summ += dic[s[i]]
                i += 1    
        return summ
