from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Initialize two pointers, one at the start, one at the end
        left = 0
        right = len(numbers) - 1

        # Move the pointers until they meet
        while left < right:
            total = numbers[left] + numbers[right]

            if total == target:
                # Found the pair, then return 1-indexed positions
                return [left + 1, right + 1]
            elif total > target:
                # Sum is too big, we move right pointer left
                right -= 1
            else:
                # Sum is too small, we move left pointer right
                left += 1
