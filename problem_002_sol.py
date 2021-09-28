
############# testbench ############# 
# n = 4
# m = 4
# a, b, d = 1, 1, 0
board = [
  [1,1,1,1],
  [1,0,0,1],
  [1,1,0,1],
  [1,1,1,1]
]
##################################### 

n, m = map(int, input().split())
a, b, d = map(int, input().split())

cnt = 1
re = 0

print("n, m", n,m)
print("a, b, d", a,b,d)

d_ = [0, 1, 2, 3] # 북, 동, 남, 서
d__ = [[-1,0], [0,1], [1,0], [0, -1]]
# board = [[0] * m for i in range(n)]

for i in range(n):
  if i == 0 or i == n-1:
    board[i] = [1]*m
  else:
    board[i][0] = 1
    board[i][-1] = 1


# 반시계 방향으로 돌았을 때
# d = d_[d_.index(d) - 1]

board[a][b] = 1

while re != 4:
  if board[a + d__[d_[d_.index(d) - 1]][0]][b + d__[d_[d_.index(d) - 1]][1]] == 0:
    re = 0
    cnt += 1
    a = a + d__[d_[d_.index(d) - 1]][0]
    b = b + d__[d_[d_.index(d) - 1]][1]
    d = d_[d_.index(d) - 1]
    board[a][b] = 1

    print("re : {}, d : {}, a : {}, b : {}". format(re, d, a, b))
  else:
    d = d_[d_.index(d) - 1]
    
    re += 1
    print("re : {}, d : {}, a : {}, b : {}". format(re, d, a, b))


print(cnt)
