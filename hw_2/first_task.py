word = str(input())
middle = len(word)//2
if len(word) % 2 == 1:
    print(word[middle])
else:
    print(word[middle-1:middle+1])
