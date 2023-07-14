student = ['engonf','fdf','df']

grades =[2,1,4]
print ("student[1]",student[1])
print("len(student)",len(student))

print("min",min(grades))
print("max",max(grades))

import statistics
print(statistics.mean(grades))
mean_grade = int(statistics.mean(grades))
print(mean_grade)
import random
print("random.choice(students)", random.choice(student))

name = 'egoing'
message = 'hi, '+name+' .... bye, '+name+'.'
print(message)