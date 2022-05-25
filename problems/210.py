from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        leaves = set(range(numCourses))
        num_edges = {i: 0 for i in range(numCourses)}
        neighbours = {i: set() for i in range(numCourses)}

        for a, b in prerequisites:
            if a in leaves:
                leaves.remove(a)
            num_edges[a] += 1
            neighbours[b].add(a)

        answer = []
        while leaves:
            leaf = leaves.pop()
            answer.append(leaf)
            for course in neighbours[leaf]:
                num_edges[course] -= 1

                if not num_edges[course]:
                    leaves.add(course)

        if len(answer) == numCourses:
            return answer

        return []




