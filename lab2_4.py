from random import randint
user_number=int(input("enter multiplication table: "))
no_of_questions=int(input("enter number of questions: "))
for x in range(no_of_questions):
    i=randint(1,10)
    print("What is",user_number,"*",i,"?")
    ans=int(input("enter answer: "))
    product=user_number*i
    print("correct answer is",product)
    
            

