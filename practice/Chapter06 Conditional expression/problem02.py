# Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user?

marks1 = int(input("Enter a subject marks: "))
marks2 = int(input("Enter a subject marks: "))
marks3 = int(input("Enter a subject marks: "))

# check the percentage 

total_percentage =(100*(marks1 + marks2 + marks3))/300
total_percentage = round(total_percentage, 2)

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3 >=33):
    print("You are Passed", total_percentage)

else:
    print("You are Fail", total_percentage)