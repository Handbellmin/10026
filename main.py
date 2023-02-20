import sys
sys.setrecursionlimit(10**6)
input =sys.stdin.readline
n = int(input())
graph = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
  str = input()
  for j in range(n):
    graph[i][j] = str[j]

x1 = [-1,1,0,0]
y1 = [0,0,-1,1]

cnt = 0
def DFS(x,y,visited,color,graph):
  visited[x][y] = True
  for i in range(4):
    x_z = x + x1[i]
    y_z = y + y1[i]
    if 0 <= x_z < n and 0 <= y_z < n and graph[x_z][y_z] == color and not visited[x_z][y_z]:
      visited[x_z][y_z] = True
      DFS(x_z,y_z,visited,color,graph)
      
visited = [[False for _ in range(n)] for _ in range(n)]
for i in range(n):
  for j in range(n):
    if not visited[i][j]:
      DFS(i,j,visited,graph[i][j],graph)
      cnt += 1

visited = [[False for _ in range(n)] for _ in range(n)]
graph1 = [[0 for _ in range(n)] for _ in range(n)]      
for i in range(n):
  for j in range(n):
    if graph[i][j] == 'G':
      graph1[i][j] = 'R'
    else:
      graph1[i][j] = graph[i][j]
cnt1 = 0
for i in range(n):
  for j in range(n):
    if not visited[i][j]:
      DFS(i,j,visited,graph1[i][j],graph1)
      cnt1 += 1
print(cnt , end = ' ')
print(cnt1)