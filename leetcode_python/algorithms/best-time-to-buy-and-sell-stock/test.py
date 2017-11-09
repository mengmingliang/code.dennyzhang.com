#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <contact@dennyzhang.com>
## Tags: #amusing, #redo, #brain
## Description:
##     https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
##    ,-----------
##    | Say you have an array for which the ith element is the price of a given stock on day i.
##    | 
##    | If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
##    | 
##    | Example 1:
##    | Input: [7, 1, 5, 3, 6, 4]
##    | Output: 5
##    | 
##    | max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
##    | Example 2:
##    | Input: [7, 6, 4, 3, 1]
##    | Output: 0
##    | 
##    | In this case, no transaction is done, i.e. max profit = 0.
##    `-----------
##
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-28 21:01:14>
##-------------------------------------------------------------------
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ## Idea: Suppose L is separated by L1 and L2.
        ##       If the max_profit happens in between L1 and L2,
        ##       it means we buy with some price in L1, then seel with some price in L2.
        ##       The buy price will be the mininum value within L1
        ##        
        ##
        ##       Here we suppose to scan the list only once
        ##
        ##       max_profit: best deal within L1
        ##       min_value: the mininum price within L1
        ##           
        ##       
        ## Complexity: Time O(n), Space O(1)
        ## Sample Data:
        ##     7, 1, 5, 3, 6, 4
        ##
        length = len(prices)
        if length < 2:
            return 0
        min_value = prices[0]
        max_profit = -1
        for i in range(1, length):
            if prices[i] < min_value:
                min_value = prices[i]
            elif prices[i] > min_value and prices[i] - min_value > max_profit:
                max_profit = prices[i] - min_value
        return max_profit if max_profit > 0 else 0            
