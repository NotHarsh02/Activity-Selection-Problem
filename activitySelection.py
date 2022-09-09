from tokenize import String


start = [1, 2, 4, 1, 5, 8, 9, 11, 13]
end = [3, 5, 7, 8, 9, 10, 11, 14, 16]
lenAct = []
order = []
reqEnd = -1
k = 0
# assume activities already sorted on end time
noOfAct = len(start)

for i in range(noOfAct):
    lenAct.append(end[i] - start[i])
    order.append(-1)
    # print(i)


for i in range(noOfAct):
    if(start[i] >= reqEnd):
        temp = start[i]
        max = lenAct[i]
        order[k] = i
        k += 1
        for j in range(i+1, noOfAct):
            if(start[j] == temp and lenAct[j] > max):
                k -= 1
                order[k] = j

                k += 1

    reqEnd = end[order[k-1]]
    # print(reqEnd)
print("The order of activities are:")
for len in order:
    if(len != -1):
        print("A"+str(len+1))
    # print(len+1)
