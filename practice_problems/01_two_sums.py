'''
Source: https://leetcode.com/problems/two-sum/ 

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

'''


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # Brute-force method -
        # Go through all elements in for loop to find complement number for target
        
        '''
        answer = list()
        for i, vals in enumerate(nums):
            first_num = vals
            first_index = i
            complement = target - first_num
            for j, vals in enumerate(nums):
                if (vals == complement and i != j):
                    answer.append([i, j])
        for i, vals in enumerate(answer):
            if (i%2 != 0):
                answer.remove(vals)
                
        return answer[0]
        
        '''
        
        #----------------------------------------------------------------#
        
       
        # More Efficient Method (2-pass hash table):
        # Check using a dictionary:
        
        # Create a dictionary that holds the key:value pair as 
        # key - value read from dictionary
        # value - index of the value in the dictionary
        
        new_dict = set()
        
        # One pass to get values into a dictionary
        new_dict = {i : nums.index(i) for i in nums}
        
        # Second Pass to retrieve the indexes in the dictionary
        for i, vals in enumerate(nums):
            # Complement is the other number to look for in the array
            # Edge Cases: 
            #   (1) do not pull up the same value in the dictionary - covered by if statement below
            #   (2) what if you have 2 threes? -- covered by set declaration above
            
            complement = target - vals
            
            if (complement in new_dict and i != new_dict[complement]):
                return [i, new_dict[complement]]
            
        return 0
        
