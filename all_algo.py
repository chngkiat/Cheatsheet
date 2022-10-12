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
    
    def longestpalindromesubstr(self,st):
        '''
        Using DP to solve longest palindromic substr problem. Stores all index as the universe of substr,
        and then always builds on top of the k-2 substr as universe until we get the longest substr
        '''
        
        n = len (st)
        
        # check if entire string is palindrome. If yes just give
        if st == st[::-1]:
            return st
        
        table = {}
        
        # First to add in all index i as the universe to search
        table[1] = [i for i in range(n)]
        maxlength = 1
        
        # Next to fill all index where substr 2 are universes
        i = 0
        start = 0
        
        table[2] = []
        while i < n-1:
            if (st[i] == st[i+1]):
                table[2].append(i)
                maxlength = 2
            i+=1
         
        # Now to fill everything else. We filter out all values which cant add 1 to the left and 1 to the right
        # Using next so that we dont end up missing out even vs odd searches.
        k = 3
        while k <= n:
            table[k] = []
            table_index = k-2
            if table[table_index] == []:
                next
            else:
                search_universe = table[table_index]
                for ele in search_universe:
                    if ele > 0 and (ele + table_index) < n:
                        if st[ele-1] == st[ele + table_index]:
                            table[k].append(ele-1)
                            maxlength = max(k,maxlength)
            k+=1
        
        start = table[maxlength][0]
        return table, st[start:(start + maxlength)]


a = Solution()