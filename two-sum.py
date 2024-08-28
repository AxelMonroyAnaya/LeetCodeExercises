"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""

class Solution():
    def __init__(self,input,target):
        self.input=input
        self.target=target
    def comprobar(self):
        if isinstance(self.input, list) and isinstance(self.target, int):
            print(f"list {self.input} target is {self.target}")
            length = len(self.input)
            for i in range(length):
                for j in range(i + 1, length):
                    res = self.input[i] + self.input[j]
                    if res == self.target:
                        print(f"output[{i},{j}]")
                        return
        else:
            print("wrong values ")
            
res = Solution([2,7,11,15], 9)
res.comprobar() 
print("\n")
res2 = Solution([3,2,4], 6)
res2.comprobar()
print("\n")
res3 = Solution([3,3], 6)
res3.comprobar()
print("\n")
