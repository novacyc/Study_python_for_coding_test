from collections import deque
import copy

def topologi_sort(indegree, lecture_time, graph):
   total = copy.deepcopy(lecture_time)
   path = list()
   q = deque()

   for i in range(1, n+1):
       if indegree[i] == 0:
           q.append(i)

   while q:
       now = q.popleft()
       path.append(now)
       for next in graph[now]:
           indegree[next] -= 1
           total[next] += lecture_time[now]
           if indegree[next] == 0:
               q.append(next)
               
   return total, path    
    
if __name__ == "__main__":
    n = int(input())
    
    graph = [[] for _ in range(n+1)]
    lecture_time = [0] * (n+1)
    indegree = [0] * (n+1)
    
    for n in range(1, n+1):
        values = list(map(int, input().split()))
        lecture_time[n] = values[0]
        for value in values[1:]:
            if value != -1:
                graph[value].append(n)
                indegree[n] += 1
    total, path = topologi_sort(indegree, lecture_time, graph) 
    print(total)
    print(path) 
      
"""
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1

graph[n] : n번 vertex에 연결된 vertex n 표시
indegree[n] : n번 vertext에 하위 vertex 수

graph : [[], [2, 3, 4], [], [4, 5], [], []]
indegree : [0, 0, 1, 1, 2, 1]
lecture : [0, 10, 10, 4, 4, 3]
"""
