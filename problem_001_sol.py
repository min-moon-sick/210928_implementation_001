
x = str(input())
cnt = 0

x_col = [0, 'a', 'b', 'c', 'd','e','f','g', 'h']

path = [
  [2, 1],
  [2, -1],
  [-2, 1],
  [-2, -1],
  [1, 2],
  [1, -2],
  [-1, 2],
  [-1, -2]
]
# x_col.index, x[1]

for i in range(len(path)):
  # path[i][0]
  # path[i][1]

    if 0 < x_col.index(x[0]) + path[i][0] < 9 and 0 < int(x[1]) + path[i][1] < 9 :
      cnt += 1

print(cnt)






