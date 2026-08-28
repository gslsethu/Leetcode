class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=[[] for _ in range(numCourses)]
        indegree=[0]*numCourses

        for course,prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegree[course]+=1
        q=deque([])
        for i in range(len(indegree)):
            if indegree[i]==0:
                q.append(i)
        count=0
        while q:
            k=q.popleft()
            count+=1
            for neighbour in graph[k]:
                indegree[neighbour]-=1
                if indegree[neighbour]==0:
                    q.append(neighbour)
        return count==numCourses

    


        