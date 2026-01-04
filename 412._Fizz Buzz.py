💻Problem link: Problem link: https://leetcode.com/problems/fizz-buzz/

💻Code:
class Solution:
    def fizzBuzz(self, n: int):
        ans = []
        
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                ans.append("FizzBuzz")
            elif i % 3 == 0:
                ans.append("Fizz")
            elif i % 5 == 0:
                ans.append("Buzz")
            else:
                ans.append(str(i))
        
        return ans

