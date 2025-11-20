from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        # Constraints:
        # 1. max two people
        # 2. each boat can hold "limit" weight

        # Sort weights so we can pair lightest + heaviest efficiently
        people.sort()

        left, right = 0, len(people) - 1
        boats = 0

        # Use two-pointer greedy approach
        while left <= right:
            # If the lightest and heaviest persons weights combined <= limit they can fit on one boat
            if people[left] + people[right] <= limit:
                left += 1  # Move left pointer further

            # The heaviest person always takes a boat (either alone or paired)
            right -= 1
            boats += 1

        return boats
