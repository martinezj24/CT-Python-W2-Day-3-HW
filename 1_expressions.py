import re
#Task 1: Name Verification

names = ["Abraham Lincoln", "Andrew P Garfield", "peter pan", "Connor Milliken", "Jordan Alexander Williams", "Madonna", "programming is cool"]


def name_check(names):
    pattern =  r'^[A-Z][a-z]*(?: [A-Z][a-z]*)*$'
    
    for name in names:
        if re.match(pattern, name):
            print(name)
        else:
            print("Invalid name")


name_check(names)