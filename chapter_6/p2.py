marks1 =int(input("enter your marks1:"))
marks2 =int(input("enter your marks1:"))
marks3 =int(input("enter your marks1:"))

total_marks=(1*(marks1+marks2+marks3))/3

if(total_marks>=40 and marks1>=33 and marks2>=33 and marks3>=33):  
    print("you are pass:",total_marks)
else:
    print("you are fail",total_marks)

