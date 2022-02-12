### activity selection problem, 
### n activities, start end times, select max number of activities


def printMaxActivities(A, n):
    ###A = [(s, f)]: an array of start/finish times
    ###n: total number of activities
    cnt = 0
    i = 0
    print("The following activities are selected ")
    for j in range(n):
        if (A[j][0] >= A[i][1]):
            print(j)
            i = j
            cnt += 1
    print("in total {}".format(cnt))

if __name__ == "__main__":
    activities = [(1,2), (0,6), (3, 4), (5, 7), (8, 9), (5, 9)]
    A = sorted(activities, key = lambda x: x[1])
    printMaxActivities(A,len(A))


