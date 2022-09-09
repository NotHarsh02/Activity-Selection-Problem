# Activity-Selection-Problem
Provides a solution for activity selection problem and follows greedy approach for the solution implemented in python 3.6


This project provides a solution for Activity Selection Problem using Greedy algorithmic approach. Greedy is a algorithmic approach which builds up solution piece by piece, these are chosen such that it is the most benificial approach, this provides a solution to optimization problems. In this aproach we make choice at every step that provides best solution at present and hence we get the optimal solution for complete problem. Activity selection problem is a approach wherein we select the activity from the set of given activities such that we maaximum number of activities should be completed/selected using the given solution

Problem Statement:
In this Activity Selection Problem we were given a problem and were expected to Modify the selecting criteria and suggest a logic to select the activity with maximum duration of resource usage.

Index	Start	End
1	     1	     3
2	     2	     5
3	     4	     7
4	     1	     8
5	     5	     9
6	     8	     10
7	     9	     11
8	     11	     14
9	     13	     16



Code:



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

Output:
The order of activities are:
A4
A6
A8


Explanation :
DATA STUCTURE USED - 
Start list: To store the start time of each activity
End list: To store the end time of each activity


The approach to my solution is simple,
Step 01 : We iterate through the start and end lists and store the difference of ith indices into the respective ith index in the lenAct list, this list stores the usage of each given activities.
Step 02 : The given data is assumed to be sorted by their end times, so we first select the activity with the least time.If their are multiple instances of the same activity,we select the activity which has the gretest duration ie.highest value in lenAct for its respective index
Step 03 : In this step, we iterate the start list and select a maximum activity from the set of activities such that the end time of each of the activities is less than the start time of the activity selected in Step 02 using conditional statements.
Step 04 : Similiar to step 03, here we select maximum activities from the set of activities such that the start time of each of the selected activities is greater than or equal to the end time of activity selected in Step 02 using conditional statements.
