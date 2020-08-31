from itertools import combinations
string = input()
stack = []
indexStack = []
setList = []
baseString = ""
lastidx = 0
for i in range(len(string)):
    s = string[i]
    if s == "(":
        stack.append("(")
        indexStack.append(i)
        baseString += string[lastidx:i]
        baseString += " "
        lastidx = i+1
    elif s==")":
        stack.pop()
        setList.append((indexStack[-1],i))
        indexStack.pop()
        baseString += string[lastidx:i]
        baseString += " "
        lastidx = i+1

baseString += string[lastidx:]

result = [baseString.replace(" ", "")]
cbs = []

for i in range(1, len(setList)):
    cbs.append(combinations(setList, i))

for cb in cbs:
    for cc in cb:
        copyString = baseString
        for c in cc:
            copyString = copyString[:c[0]] + "(" + copyString[c[0]+1:c[1]] + ")"
            if c[1] != len(string) - 1:
                copyString += baseString[c[1]+1:]
        result.append(copyString.replace(" ", ""))


result = list(set(result))
result.sort()

for i in result:
    print(i)