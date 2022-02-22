input1 = input()
lst1 = set(sorted(list(input1), reverse = True))
temp = ''
for i in lst1:
	temp+=i+str(input1.count(i))
print(temp)


