#!/usr/bin/env python3


#------------------------------------------------------------------------------------------------------------------------------------
#
#   Write a Python program to print all distinct values in a dictionary.
#   Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
#   Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}
#
#------------------------------------------------------------------------------------------------------------------------------------

ml = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]

unique_values = set(v for i in ml for v in i.values())


print(unique_values)

