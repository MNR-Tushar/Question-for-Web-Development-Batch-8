total_point=0

def L_grade(point):
    if point>=5.00:
        return "A+"
    elif point>=4.00:
        return "A"
    elif point>=3.5:
        return "A-"
    elif point>=3.00:
        return 'B'
    elif point>=2.00:
        return "C"
    elif point>=1.00:
        return "D"
    else:
        return "F"
    

def Grade(m):
    global total_point
    if m>=80:
        total_point+=5.00
        return "A+"
    elif m>=70:
        total_point+=4
        return "A"
    elif m>=60:
        total_point+=3.5
        return "A-"
    elif m>=50:
        total_point+=3
        return 'B'
    elif m>=40:
        total_point+=2
        return "C"
    elif m>=33:
        total_point+=1
        return "D"
    else:
        total_point+=0
        return "F"

print("Student Grade Calculator")
while True:
    marks=[]
    subject_name=[]

    try:
        name=input("Enter Your Name: ")
        total_sub=int(input("How many subjects: "))

        try:
            for i in range(0,total_sub):
                subject_name.append(input("Enter your Subject name: "))
                marks.append(int(input(f"Enter your {subject_name[i]} mark: ")))

            while marks[i]<0 or marks[i]>100:
                print("Please input mark between 0-100")
                marks[i]=int(input(f"Enter your {subject_name[i]} mark: "))
        except:
            print("Invalid Mark")
            continue

        #Display student information
        print(f"\nStudent Name: {name}")
        print("Grade All Subject")
        print("----------------------")
        for sub in range(0,total_sub):
            print(f"Grade of {subject_name[sub]} : {Grade(marks[sub])}")
            G=total_point/total_sub
        print("----------------------")
        print(f"GPA: {G} Grade: {L_grade(G)}")
        print("\n")

    except:
        print("\nInvalid Total Subject\n")
    
    total_point=0
   


