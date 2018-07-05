# Leetcode: Peeking Iterator     :BLOG:Medium:


---

Peeking Iterator  

---

Similar Problems:  
-   [Review: Object-Oriented Design Problems](https://code.dennyzhang.com/review-oodesign)
-   Tag: [oodesign](https://code.dennyzhang.com/tag/oodesign)

---

Given an Iterator class interface with methods: next() and hasNext(), design and implement a PeekingIterator that support the peek() operation &#x2013; it essentially peek() at the element that will be returned by the next call to next().  

Here is an example. Assume that the iterator is initialized to the beginning of the list: [1, 2, 3].  

Call next() gets you 1, the first element in the list.  

Now you call peek() and it returns 2, the next element. Calling next() after that still return 2.  

You call next() the final time and it returns 3, the last element. Calling hasNext() after that should return false.  

Follow up: How would you extend your design to be generic and work with all types, not just integer?  

Credits:  
Special thanks to @porker2008 for adding this problem and creating all test cases.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/peeking-iterator)  

Credits To: [leetcode.com](https://leetcode.com/problems/peeking-iterator/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/peeking-iterator
    ## Basic Ideas: Use a variable to cache the peek. Always pre-cache
    ##
    # Below is the interface for Iterator, which is already defined for you.
    #
    # class Iterator(object):
    #     def __init__(self, nums):
    #         """
    #         Initializes an iterator object to the beginning of a list.
    #         :type nums: List[int]
    #         """
    #
    #     def hasNext(self):
    #         """
    #         Returns true if the iteration has more elements.
    #         :rtype: bool
    #         """
    #
    #     def next(self):
    #         """
    #         Returns the next element in the iteration.
    #         :rtype: int
    #         """
    
    class PeekingIterator(object):
        def __init__(self, iterator):
            """
            Initialize your data structure here.
            :type iterator: Iterator
            """
            self.iterator = iterator
            if self.iterator.hasNext():
                self.peek_element = self.iterator.next()
    
        def peek(self):
            """
            Returns the next element in the iteration without advancing the iterator.
            :rtype: int
            """
            return self.peek_element        
    
        def next(self):
            """
            :rtype: int
            """
            res = self.peek_element
            if self.iterator.hasNext():
                self.peek_element = self.iterator.next()
            else:
                self.peek_element = None
            return res
    
        def hasNext(self):
            """
            :rtype: bool
            """
            return (self.peek_element is not None)
    
    # Your PeekingIterator object will be instantiated and called as such:
    # iter = PeekingIterator(Iterator(nums))
    # while iter.hasNext():
    #     val = iter.peek()   # Get the next element but not advance the iterator.
    #     iter.next()         # Should return the same value as [val].