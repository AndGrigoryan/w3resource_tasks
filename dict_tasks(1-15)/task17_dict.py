#!/usr/bin/env python3

#---------------------------------------------------------------------------------------------
#
#    Write a Python program to remove duplicates from the dictionary.
#
#---------------------------------------------------------------------------------------------

md = {'id1': 
   {'name': ['Sara'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id2': 
  {'name': ['David'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id3': 
    {'name': ['Sara'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id4': 
   {'name': ['Surya'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
}


result = {}

for k, v in md.items():
    if v not in result.values():
        result[k] = v

print(result)

