#!/usr/bin/env python3

#---------------------------------------------------------------------------------------------
#
#    Write a Python script to concatenate the following dictionaries to create a new one.
#
#   Sample Dictionary :
#   dic1={1:10, 2:20}
#   dic2={3:30, 4:40}
#   dic3={5:50,6:60}
#   Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
#
#---------------------------------------------------------------------------------------------

dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}
dic4 = {}

for k, v in dic1.items():
    dic4[k] = v

for k, v in dic2.items():
    dic4[k] = v

for k, v in dic3.items():
    dic4[k] = v

print(dic4)

