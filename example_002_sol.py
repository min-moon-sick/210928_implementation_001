N = int(input())
cnt = 0

for i in range(N + 1):
  
  for ii in range(60):
    for iii in range(60):
      if '3' in str(i) + str(ii) + str(iii):
        cnt += 1
  print(" cnt : ", cnt)

print(cnt)
