def three_sum(array):
    # brute force
    triplets = set()
    n = len(array)

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if array[i] + array[j] + array[k] == 0:
                    temp = [array[i], array[j], array[k]]
                    temp.sort()
                    triplets.add(tuple(temp))

    return list(triplets)


print("Test 1: [-1, 0, 1, 2, -1, -4] :", three_sum([-1, 0, 1, 2, -1, -4]))
#  [[-1,-1,2],[-1,0,1]]
