from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the array to use two-pointer technique
        nums.sort()
        answer = []

        # Iterate through each number, treating it as the fixed first element
        for i in range(len(nums)):

            # Skip duplicate first elements to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Two pointers for the remaining part of the array
            left = i + 1
            right = len(nums) - 1

            # Move left and right pointers to find two numbers that sum to -nums[i]
            while left < right:
                amount = nums[i] + nums[left] + nums[right]

                if amount < 0:
                    # Need a larger sum, so move left pointer to the right
                    left += 1
                elif amount > 0:
                    # Need a smaller sum, so move right pointer to the left
                    right -= 1
                else:
                    # a valid triplet
                    answer.append([nums[i], nums[left], nums[right]])

                    # Move left pointer forward
                    left += 1

                    # Skip duplicate values for left pointer
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return answer
