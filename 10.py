grades=[]
num=float(input("enter the first grade: "))
grades.append(num)
num=float(input("enter the second grade: "))
grades.append(num)
num=float(input("enter the thrid grade: "))
grades.append(num)
minimumgrade=min(grades)
grades.remove(minimumgrade)
minimumgrade=min(grades)
grades.remove(minimumgrade)
average=sum(grades)/len(grades)
print("average grade: {0:.2f}".format (average))
      
