#Problem 15#
row = 20
col = 20
grid = [[0 for a in range(col+1)] for b in range(row+1)]

for c in range(0,row+1):
  grid[c][0]=1
  for d in range(1,col+1):
    grid[0][d]=1

for e in range(1,row+1):
  for f in range(1,col+1):
    grid[e][f]=grid[e-1][f]+grid[e][f-1]


for z in grid:
    print(z)
print()

total=int(grid[row][col])
print("Number of routes for a " + str(row) + "x" + str(col) + " grid: " + str(total))

