"""
TC -> O(V+E)
SC -> O(V+E)
Logic
We use topological sorting to find if a course schedule is valid/ not valid.
Steps:
1. Construct adjacency list
2. Compute indegree and add to queue if indegree of a node is 0. This means the course is independent
3. Iterate the loop and for each course, find the adjacent courses, reduce the indegree and add to queue if indegree becomes 0.
4. While iterating the queue, every time you pop, increment the count variable.
5. If count equals numCourses, it means schedule is valid. If it is not, it means a cycle exists and hence schedule is invalid
"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        indegree = [0] * numCourses
        queue = []
        count = 0
        for v, u in prerequisites:
            adj_list[u].append(v)
        for key in adj_list.keys():
            for val in adj_list[key]:
                indegree[val] += 1
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            course = queue.pop(0)
            count += 1
            for neigh in adj_list[course]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    queue.append(neigh)
        return count == numCourses
