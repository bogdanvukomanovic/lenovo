from typing import List

class Solution:

    # def longestCommonPrefix(self, strs: List[str]) -> str:
        
    #     n = len(strs)

    #     i, j = 0, 0 
    
    #     s, prefix = "", ""
        
    #     while True:

    #         if len(strs[i]) == 0:
    #             return ""
            
    #         if len(strs[i]) == j:
    #             return prefix 
            
    #         if s == "":
    #             s = strs[i][j]
    #             i += 1
    #         else:
    #             if s == strs[i][j]:
    #                 i += 1
    #             else:
    #                 return prefix

    #         if i % n == 0:
    #             prefix += s
    #             i = 0
    #             j += 1
    #             s = ""

    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        min_w = min(strs)
        max_w = max(strs)

        for i in range(0, len(min_w)):
            if min_w[i] != max_w[i]:
                min_w = min_w[:i]
                break

        return min_w

solution = Solution()
print(solution.longestCommonPrefix(["flower","flow","flight"]))

'''
    Let A be a set that represents the English lowercase alphabet.
    We can define function, g : A -> N, which maps letter to a natural number:
        g(a) = 1, g(b) = 2, ..., g(z) = 26
    Also, for empty word case, let's say that g('') = 0.

    Let w_1 = x_1|x_2|...|x_n and w_2 = y_1|y_2|...|y_m be two words (0 < n <= m) that have common prefix of length k (0 < k < n).

        w_1 = x_1|x_2|...|x_k|x_k+1|...|x_n
        w_2 = y_1|y_2|...|y_k|y_k+1|...|y_m

    We say that:
        w_1 < w_2 iff g(x_k+1) < g(y_k+1)
        w_1 > w_2 iff g(x_k+1) > g(y_k+1)
        w_1 = w_2 iff g(x_k+i) = g(y_k+i), n = m, i \in {1, ..., n-k}
    If we remove the common prefix from both words:
        w_1 = x_k+1|...|x_n
        w_2 = y_k+1|...|y_m
    the relation still holds.

    Note that if for example w1 = '', w1 = w2 iff w2 = '', otherwise w2 > w1.
    
    In this problem, we are given set of words T. Let's say that |T| = t. 
    
    Let's define w_min and w_max words with the following feature:
        w_min = {x | x <= w, w \in T} 
        w_max = {x | x >= w, w \in T}
    
    If all of the words from T start with the prefix P = p_1|p_1|...|p_k it is clear 
    that w_min and w_max will have the same prefix.
    If some of the words do not share the prefix p, w_min and w_max will start with
    the different letters.
'''