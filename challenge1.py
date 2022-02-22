input1 = input()
ans = ''
for i in range(0,len(input1)-1,2):
	ans+=input1[i]*int(input1[i+1])
print(ans)
