from operator import itemgetter
from collections import deque

def getdistance(cities, src, dst):
    s = cities[src]
    d = cities[dst]
    return abs(s[1] - d[1]) + abs(s[2] - d[2])

def closestspecial(cities, src):
    s = cities[src]
    m = [2000, s]
    for i in range(len(cities)):
        if cities[i][0] == 1:
            d = getdistance(cities, src, i)
            if d < m[0]:
                m = [d, i]
    return m


def findmin(cities, src, dst, T):
    realdist = getdistance(cities, src, dst)
    s = closestspecial(cities, src)
    d = closestspecial(cities, dst)
    virtdist = s[0] + d[0] + T

    return min([realdist, virtdist])

n, t = map(int, input().split())
cities = []
for i in range(n):
    cities.append(list(map(int, input().split())))

for i in range(n):
    c = cities[i]
    cities[i] = [c[0], c[1], c[2], True]

m = int(input())
want = []
for i in range(m):
    src, dst = map(int, input().split())
    print(findmin(cities, src-1, dst-1, t))