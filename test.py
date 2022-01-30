
import numpy as np
import lab
import matplotlib.pyplot as plt
import random

max = 100
divide = 10

xData = [i for i in range(int(max/divide))]
yData = [random.randint(i-divide,i) for i in range(0,max,divide)]
xError = [random.randint(0,1) for i in range(int(max/divide))]
yError = [random.randint(5,10) for i in range(int(max/divide))]
ax = lab.scattergraph(xData,yData, yError = yError,xError = 0,error_label = "Error Uncertainty", data_label = "Data")
plt.show()

# l = [2,3,4,4,7,7,6]
# o = "123"
# x = "False" in [x.isdigit() for x in o]
# a = "xyaabbbccccdefww"
# b = "xxxxy//yabklmopq"
# b = 'www.google.com'
# print(b.split("//")[-1])
# print(b.split("//")[-1].split("www.")[-1])
# print(b.split("//")[-1].split("www.")[-1].split("."))

# def order(sentence):
#     return " ".join(sorted(sentence.split(), key=lambda x: [int(x) for x in list(filter(str.isdigit, x))]))

# p = "4of Fo1r pe6ople g3ood th5e the2"


# o = [5,5,3,4,32,4,2,4,4,4,3,4,3]
# o.sort()
# print(set(o))
# # print([chr(x) for x in range(ord('a'),ord('z')+1)])

# data = []
# for _ in range(int(input())):
#     name = input()
#     score = float(input())6
#     data.append([name,score])
    
# second_lowest_score = sorted(set([x[1] for x in data]))[1]
# names_of_second_lowest = [x[0] for x in data if(x[1]== second_lowest_score)]
# for i in range(len(names_of_second_lowest)):
#     print(names_of_second_lowest[len(names_of_second_lowest)-1-i])


# a = []
# bigList = []

# count = -1
# for i in range(0,40):
#     for j in range(0,40):
#         count += 1
#         a.append(count)
#     if(len(a)==40):
#         bigList.append(a)
#         a= []

# print(bigList[39][39])
