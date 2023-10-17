sol = SolverFor("QF_FD")


# data
m = 16
n = 8

# Note: 1-based
graph_1_based = [[1, 2],
                [1, 3],
                [1, 4],
                [2, 3],
                [2, 4],
                [3, 4],
                
                [5, 6],
                [5, 7],
                [5, 8],
                [6, 7],
                [6, 8],
                [7, 8],
                
                [1, 5],
                [2, 6],
                [3, 7],
                [4, 8]]

# Adjust to 0-based
graph = [ [graph_1_based[i][0]-1, graph_1_based[i][1]-1] for i in range(m)]
print(graph)

# variables
nodes = makeIntVector(sol,"nodes",n,0,m)
# nodes = [Int(f"nodes[{i}]") for i in range(n)]
# for i in range(n):
#     sol.add(nodes[i] >= 0, nodes[i] <= m)

edges = makeIntVector(sol,"edges",m,1,m)
# edges = [Int(f"edges[{i}]") for i in range(m)]
# for i in range(m):
#     sol.add(edges[i] >= 0, edges[i] <= m-1)

# constraints
for i in range(m):
    sol.add(Abs(nodes[graph[i][0]] - nodes[graph[i][1]]) == edges[i])

sol.add(Distinct(edges))
sol.add(Distinct(nodes))

# print(sol)

num_solutions = 0
print("solve")
while sol.check() == sat:
  num_solutions += 1
  mod = sol.model()
  print("nodes:", [mod.eval(nodes[i]) for i in range(n)])
  print("edges:", [mod.eval(edges[i]) for i in range(m)])  
  print()
  getDifferentSolution(sol,mod,edges,nodes)

print("num_solutions:", num_solutions)