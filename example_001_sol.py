def Right(y, N):
  return y + 1 if y + 1 <= N  else y

def Left(y, N):
  return y - 1 if 0 < y - 1 else y

def Up(x, N):
  return x - 1 if 0 < x - 1  else x

def Down(x, N):
  return x + 1 if x + 1 <= N  else x

N = input()

path = list(map(str, input().split()))

print(N)
print(path)

N = int(N)
x = 1
y = 1
i = 0

for i in range(len(path)):
  
  print("i :", i)
  print("path[i]", path[i])

  if path[i] == 'r':
    y = Right(y, N)
  elif path[i] == 'l':
    y = Left(y, N)
  elif path[i] == 'u':
    x = Up(x, N)
  else:
    x = Down(x, N)


print("x : {}, y :{}".format(x, y))
