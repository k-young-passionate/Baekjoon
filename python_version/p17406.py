from itertools import permutations

def getinput():
    n, m, k = map(int, input().split())

    mat = []
    for _ in range(n):
        mat.append(list(map(int, input().split())))

    rot = []
    for _ in range(k):
        rot.append(list(map(int, input().split())))

    return n, m, k, mat, rot


def rotateandmin(mat, rot):
    points = [rot[0]-rot[2]-1, rot[1]-rot[2]-1, rot[0]+rot[2]-1, rot[1]+rot[2]-1]
    for k in range(rot[2]):
        r1 = mat[points[0]+k][points[1]+k:(points[3]+1-k)].copy()
        r1 = r1[:-1]
        r1.insert(0, mat[points[0]+1+k][points[1]+k])
        r2 = mat[points[2]-k][points[1]+k:points[3]+1-k].copy()
        r2 = r2[1:]
        r2.append(mat[points[2]-k-1][points[3]-k])

        c1 = [x[points[1]+k] for x in mat[points[0]+k:points[2]-k+1]]
        c2 = [x[points[3]-k] for x in mat[points[0]+k:points[2]-k+1]]
        c1 = c1[1:]
        c1.append(mat[points[2]-k][points[1]+k+1])
        c2 = c2[:-1]
        c2.insert(0, mat[points[0]+k][points[3]-k-1])

        for i in range((rot[2]-k)*2+1):
            mat[points[0]+k][points[1]+i+k] = r1[i]
            mat[points[2]-k][points[1]+i+k] = r2[i]
            mat[points[0]+i+k][points[1]+k] = c1[i]
            mat[points[0]+i+k][points[3]-k] = c2[i]
    candidate = []
    for i in mat:
        candidate.append(sum(i))
    return min(candidate)


def debug(mat):
    for i in mat:
        print(i)
    print("================")


def test(mat, rot):
    cases = permutations(rot, len(rot))

    results = []
    for c in cases:
        tmpresult = []
        mat2 = []
        for i in mat:
            tmp = i.copy()
            mat2.append(tmp.copy())

        for i in c:
            tmpresult.append(rotateandmin(mat2, i))
        results.append(tmpresult[-1])

    return min(results)


if __name__ == "__main__":
    n, m, k, mat, rot = getinput()
    print(test(mat, rot))
