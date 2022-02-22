ans = input()
words = [word.lower() for word in ans.split()]
words.sort()
for word in words:
   print(word, end=' ')