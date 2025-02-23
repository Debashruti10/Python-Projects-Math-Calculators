def sum_of_ints(seq1,seq2):
    sum=0
    for i in seq1:
        sum=sum+i
    for j in seq2:
        sum=sum+j
    return sum
print("sum_of_ints((1,4,2) ,(2,-1))->",sum_of_ints((1,4,2) ,(2,-1)))
print("sum_of_ints((4,4,4,4) ,())->",sum_of_ints((4,4,4,4) ,()))
print("sum_of_ints((4,4) ,(4,4))->",sum_of_ints((4,4) ,(4,4)))


