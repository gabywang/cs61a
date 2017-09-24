# My comprehension of Towers of Hanoi  

To solve this problem, we simply need to consider two cases:
- The simpliest case: n = 1.
- Consider the relationship between n and (n-1).

It's obvious that for case n, the last step is to move from its __current place__ to the __end__. 
Hence, case n-1 should be in the alternative place. The order should be:
- n-1 move to the alternative place.
- n move to the end. And we have `print_move(start, end)`
- n-1 move from the alternative place to the end.

Hope this may help you have a better comprehension of Q2.
