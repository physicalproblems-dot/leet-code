


















#! Explanation
#! Bottom-up dynamic algorithm 
#! This simple idea — of remembering the past to solve the future faster — forms the core of DP
#!Dynamic Programming is a commonly used algorithmic technique used to optimize recursive solutions when same subproblems are called again.
#!The core idea behind DP is to store solutions to subproblems so that each is solved only once.
#!To solve DP problems, we first write a recursive solution in a way that there are overlapping subproblems in the recursion tree (the recursive function is called with the same parameters multiple times).
#!To make sure that a recursive value is computed only once (to improve time taken by algorithm), we store results of the recursive calls.
#!There are two ways to store the results, one is top down (or memoization) and other is bottom up (or tabulation).
#! Dynamic Programming (DP) is a method used to solve complex problems by breaking them into smaller overlapping subproblems and storing their results to avoid recomputation. It is an optimization technique that transforms recursive solutions with exponential time into efficient ones with polynomial time.