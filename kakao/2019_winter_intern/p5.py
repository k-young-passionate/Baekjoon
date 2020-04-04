def check(stones, k):
    cnt = 0
    index = 0
    flag = False
    for i in stones:
        if i == 0:
            cnt += 1
        else:
            cnt = 0
        if cnt == k:
            flag = True
            break
        index += 1
    return flag, index

def getsum(stones, k):
    m = sum(stones)
    for i in range(len(stones)-k+1):
        tmpset = stones[i:i+k]
        mm = max(tmpset)
        if m > mm:
            m = mm
    return m

def solution(stones, k):
    st = stones.copy()
    while True:
        st = [ s // 2 for s in st]
        flag, index = check(st, k)
        # print(st)
        # print(stones[index-k+1:index+1])
        if flag:
            answer = max(stones[index-k+1:index+1])
            break
    # print(m, mset)
    return answer