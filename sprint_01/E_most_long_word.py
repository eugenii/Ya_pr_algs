# E - Most Long Word

length = int(input())
words = input().strip().split()
longest = max(words, key=len)
print(longest, len(longest), sep='\n')