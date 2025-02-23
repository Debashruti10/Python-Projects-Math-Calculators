def average(numbers):
     sum=0
     for i in numbers:
          sum=sum+i
     avg=int(sum/len(numbers))
     return avg
print("average(1,4,4)->",average((1,4,4)))
print("average(4,4,4,4)->",average((4,4,4,4)))
print("average(-2,2)->",average((-2,2)))
