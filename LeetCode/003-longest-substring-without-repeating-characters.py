class Solution(object):
    def lengthOfLongestSubstring(self, s):
        i=0
        n = len(s)
        max_length = 0
        s_dict = {}
        count=0

        while i < n:
            if s[i] not in s_dict:
                s_dict[s[i]] = i
                count+=1
                i+=1    
            else:   
                count=0
                i = s_dict[s[i]] +1
                s_dict={}
            max_length = max(count,max_length)
        return  max_length