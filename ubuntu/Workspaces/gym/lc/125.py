class Solution:

    def isPalindrome(self, xs: str) -> bool:
        
        n = len(xs) - 1
        l, r = 0, len(xs) - 1

        while l < r:

            while l <= n and not xs[l].isalnum():
                l += 1
            
            while r >= 0 and not xs[r].isalnum():
                r -= 1

            if not (l < r and l >= 0 and r <= len(xs) - 1):
                break

            if xs[l].lower() != xs[r].lower():
                return False

            l += 1
            r -= 1
        
        return True

xs = "A man, a plan, a canal: Panama"
# xs = "race a car"
# xs = "0P"
# xs = "2 1 1 2 "
# xs = ".,"
# xs = "......"
print(Solution().isPalindrome(xs))