n = int(input())

words = []

for i in range(n):
    word = input()
    if word not in words:
        words.append(word)

words.sort(key=lambda item: (len(item), item))

for w in words:
    print(w)