n = 5
ans = 1
for i in range(1, n+1):
	ans*=i
ans = str(ans)
print(ans.count('0'))