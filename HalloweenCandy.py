#************************************************************************************************
#Problem:A few couples of attributes are distributed by the sigmoid function (with a few        *
#outliers). Therefore, we can predict that some attributes of the new type of candy aren't in   *
#training data set.                                                                             *
#                                                                                               *
#My team:                                                                                       *
#   Nguyen Dang Cuong - 1811640                                                                 *
#   Pham Quoc Trung   - 1814522                                                                 *
#   Truong Cong Thanh - 1814036                                                                 *
#                                                                                               *
#                                                                       seminar 01: 23/11/2019  *
#************************************************************************************************


import numpy as np
import csv

EPSILON = 20

def sigmoid(s):
    return 1/(1+np.exp(-s))


#load data from csv         mean = data.values.
def loadData(fileName,data):
    #data = {}
    with open(fileName) as csvFile:
        read = csv.reader(csvFile)
        count = 0
        _column = []
        member = []
        column = {}
        for row in read: 
            if count == 0:
                for item in row:
                    if (item!= row[0]):
                        column.setdefault(item,0)
                        _column.append(item)
            else:
                myType = {}
                for item in _column:
                    myType.setdefault(item,0)
                data.setdefault(row[0],myType)
                member.append(row[0])
                i = -1
                for item in row:
                    if (item != row[0]):
                        data[row[0]][_column[i]] = item
                    i = i +1
            count = count + 1
    return (_column,member)
#find sigmoid function




#       main function:
data = {}
column,members = loadData('data.csv',data)

#classify Attributes
binaryType = []
percentType = []
firstMember = data[members[0]]

for item in column:
    value = firstMember[item]
    if (value == '0') | (value == '1'):
        binaryType.append(item)
    else:
        percentType.append(item)

# Create a dictionary contain couples of attributes are distributed by the sigmoid function (guess)
guess = {}
flag = {}
for item in percentType:
    flag.setdefault(item,False)
for binary in binaryType:
    for percent in percentType:
        isOK = 0
        for mem in members:
            _bin = int(data[mem][binary])
            _per = float(data[mem][percent])
            value = sigmoid(_per - 0.5)
            if value > 0.5: 
                value = 1
            else:
                value = 0
            if value != _bin: 
                isOK = isOK + 1
        if (isOK <= EPSILON):
            if flag[percent] == False:
                flag[percent] = True
                L = []
                guess.setdefault(percent,L)
            guess[percent].append(binary)

print('Sigmoid function is right for:')
L = []
for item in guess:
    L.append(item)
    print('\t',end='')
    print(item,end = ': ')
    print(guess[item])
print('epsilon = ',EPSILON)

#Guess new input
print('Options:')
for i in range(len(L)):
    print('\t' + str(i) + ': ',L[i])

while True:
    p = int(input())
    if (p < len(L)):
        s = float(input('new ' + L[p] + ': '))
        value = sigmoid(s)
        print('GUEST:')
        if s > 0.5:
            for i in guess[item]:
                print('\t' + i + ' = 1')
        else:
            for i in guess[item]:
                print('\t' + i + ' = 0')
        break
    else:
        print('Invalid, Keep trying!')



print('B')
