
def average(marks,total_sub):
    sum=0
    for i in marks:
        sum=sum+i
    try:
        return sum/total_sub
    except Exception as e:
        print("Please, Write down total subject greater than \"0\"")

def Grade(m):
    if m>=80 and m<=100:
        return "A+"
    elif m>=70 and m<=79:
        return "A"
    elif m>=60 and m<=69:
        return "A-"
    elif m>=50 and m<=59:
        return 'B'
    elif m>=40 and m<=49:
        return "C"
    elif m>=33 and m<=39:
        return "D"
    else:
        return "F"
print("Student Grade Calculator")
while True:
    marks=[]
    subject_name=[]
    name=input("Enter Your Name: ")
    total_sub=int(input("How many subjects: "))

    for i in range(0,total_sub):
        subject_name.append(input("Enter your Subject name: "))
        marks.append(int(input(f"Enter your {subject_name[i]} mark: ")))
    
        while marks[i]<0 or marks[i]>100:
            print("Please input mark between 0-100")
            marks[i]=int(input(f"Enter your {subject_name[i]} mark: "))

    
    print("\nAverage Marks: ",average(marks,total_sub))
    
    for sub in range(0,total_sub):
        print(f"Grade of {subject_name[sub]} : {Grade(marks[sub])}")
    
    print("\n")


