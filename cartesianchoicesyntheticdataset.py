import numpy
import random
def cartesian_choice(*iterables):
    res=[]
    for population in iterables:
        res.append(random.choice(population))
    return res    
firstname=["jack","jim","john","tom","hop","max","el","moe","ron","nick"]
lastname=["byers","hopper","douglas","sinclair","wheeler","harrington","bing","geller","buffay","greene"]
number_of_specialists=15
employees=set()
while len(employees)<number_of_specialists:
    employee=cartesian_choice(firstname,lastname)
    employees.add(" ".join(employee))
print(employees)    
    
