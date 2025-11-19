from collections import deque
from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        n, m = len(maze), len(maze[0])
        sr, sc = entrance
        visited = set()
        visited.add((sr, sc))  # mark entrance as visited

        q = deque([(sr, sc, 0)])  # (row, col, distance)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # 4 movement directions

        while q:
            # pop position to explore from
            row, column, distance = q.popleft()

            # explore all four directions (move by -+ 1)
            for dr, dc in directions:
                next_row, next_col = row + dr, column + dc

                # valid cell, not visited, and open path
                if (
                    0 <= next_row < n
                    and 0 <= next_col < m
                    and maze[next_row][next_col] == "."
                    and (next_row, next_col) not in visited
                ):

                    # if boundary cell, return distance + 1
                    if (
                        next_row == 0
                        or next_row == n - 1
                        or next_col == 0
                        or next_col == m - 1
                    ):
                        return distance + 1

                    # otherwise continue BFS
                    visited.add((next_row, next_col))
                    q.append((next_row, next_col, distance + 1))

        return -1  # no exit found
