ans ='welcome to sirius india team'
temp = ''
lst = []
for i in range(len(ans)):
	temp+=ans[i]
	if ans[i]==' ':
		lst.append(temp)
		temp = ''
maximum = lst[0]
for i in range(1, len(lst)):
	if len(lst[i]) > len(maximum):
		maximum = lst[i]
	
print(maximum, len(maximum)-1)