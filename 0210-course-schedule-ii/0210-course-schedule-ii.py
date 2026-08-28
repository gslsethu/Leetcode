class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph=[[] for _ in range(numCourses)]
        indegree=[0]*numCourses

        for course,prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegree[course]+=1
        q=deque([])
        for i in range(len(indegree)):
            if indegree[i]==0:
                q.append(i)
        L=[]
        while q:
            k=q.popleft()
            L.append(k)
            for neighbour in graph[k]:
                indegree[neighbour]-=1
                if indegree[neighbour]==0:
                    q.append(neighbour)
        return L if len(L) == numCourses else []