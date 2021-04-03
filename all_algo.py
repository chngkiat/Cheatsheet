class Solution:
    def longestUniqueSubsttr(self, s):
        '''
        Finds length of Longest Unique Substring in String using start and end index. Solution is O(n) 
        Inputs: s --> type: String : A String to search for longest substring
        Output: Integer: The length of longest substring
        '''
        last_idx = {} # for hashing all the final index when scanning
        max_len = 0
        start_idx = 0
     
        for i in range(0, len(s)):
            if s[i] in last_idx:
                start_idx = max(start_idx, last_idx[s[i]] + 1) # Retrieve where the last noted starting index of the current letter is as its a repeat
            max_len = max(max_len, i-start_idx + 1) # Find the length between the 2 repeated letters or adding one if its not a repeat
            last_idx[s[i]] = i # hashing the position of the current letter
        return max_len

    def maxCumSumInList(self,l):
        '''
        Uses Kadanes Algorithm to compute the maximum cumulative sum. 
        Inputs: l --> type: list : A list of values for computing cumulative sum
        Output: Float: The maximum cumsum in the list
        '''
        max_cumsum = 0
        current_cumsum = 0
        for values in l:
            current_cumsum = max(0, current_cumsum + values)
            max_cumsum = max(max_cumsum, current_cumsum)
        return max_cumsum