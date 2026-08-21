from collections import deque
import heapq
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        ans = []

        for course, prerequisite in prerequisites:
            adj[prerequisite].append(course)
            indegree[course] += 1

        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            current = queue.popleft()
            ans.append(current)

            for course in adj[current]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    queue.append(course)

        return len(ans) == numCourses

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        ans = []

        for course, prerequisite in prerequisites:
            adj[course].append(prerequisite)
            indegree[course] += 1

        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        processed = 0
        while queue:
            current = queue.popleft()
            ans.append(current)
            processed += 1

            for course in range(numCourses):
                if current in adj[course]:
                    indegree[course] -= 1

                    if indegree[course] == 0:
                        queue.append(course)

        return ans if processed == numCourses else []

    def scheduleCourse(self, courses: List[List[int]]) -> int:
        ans = []
        curr = 0

        courses.sort(key=lambda c: c[1])
        for dur, ld in courses:
            heapq.heappush(ans,-dur)
            curr += dur
            if curr > ld:
                curr += heapq.heappop(ans)
        return len(ans)