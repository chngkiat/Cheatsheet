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

    def longestValidParentheses(self, s: str) -> int:
        """
        Uses a stack to trace the positions of all open parenthesis and slowly remove the valid parenthesis from the back. Can be used 
        for 1 and 0 pair matchings

        Inputs: s --> String: string of parenthesis to identify and check
        Output: Integer: Max length of valid parenthesis
        """
        max_len = 0
        stack = [-1]
        for i in range(len(s)):
            if s[i] == "(":
                
                stack.append(i)
            else:
                if stack and stack[-1]!=-1 and s[stack[-1]] == "(":
                    stack = stack[:-1]
                    max_len = max(max_len, i - stack[-1])
                else:
                    stack.append(i)
        return max_len

    def maxprofit2(self, ts: list) -> int:
        '''
        Uses cumulative sum to find the maximum profits from 2 trades with buy - sell - buy - sell structure. Can be extended to 
        3 trades and more, though we will need more indexes so no overlapping occurs.

        Input ts --> list: List of closing prices to compute the 2 trade max profit
        Output: Integer: Max profit attainable in the time series using 2 trades
        '''
        n = len(ts)
        profit = []
        for i in range(1,n):
            profit += [ts[i]-ts[i-1],]
        max_profit = 0
        for i in range(n-1):
            peak_profits = self.maxCumSumInList(profit[:i]) + self.maxCumSumInList(profit[i:n-1])
            max_profit = max(max_profit,peak_profits)
        return max_profit
    
    def peakvalley(self,ts:list) -> int:
        '''
        Uses cumulative sum to find the maximum profits from unlimited trades with no overlapping structure. 

        Input ts --> list: List of closing prices to compute the 2 trade max profit
        Output: Integer: Max profit attainable in the time series.
        '''
        n = len(ts)
        profit = 0
        for i in range(1 , n):
            profits = ts[i] - ts [i-1]
            profit += max(0,profits)
        return profit