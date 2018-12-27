# Semeter Grades
# semester_grades.py
# lists and list methods
# calculates the semester grades based on 5 tests for Professor Einstein

print("""
                    WELCOME TO PROFESSOR EINSTEIN'S
                      SEMESTER GRADES CALCULATOR!
""")

# ***** Initalize variables and lists *****
students=[]
grade_ave=[]
another="y"

while another == "y":
    # ***** Get student name and add to student list *****
    students.append(input("What is the student's first name?: ").title())
    
    # ***** Get student scores for 5 assignments and add to grade list *****
    student_grades=[]
    for i in range(1,6):
        student_grades.append(int(input("What is the student's test #" + str(i) + " grade: "))) 
    
    # ***** Sort & display student scores *****
    print ("\nThese are the students grades listed from high to low:")
    student_grades.sort()
    student_grades.reverse()
    for grd in student_grades:
        print (grd)
        
    # ***** Delete lowest grade *****
    print ("\nThe professor drops the lowest grade, these are the students 4 best grades:")
    del student_grades[4]
    
    # ***** Accumulate student's grades to calculate average *****
    student_grade_total=0
    for j in student_grades:
        print (j)
        student_grade_total+=j
    student_grade_ave=student_grade_total/4
    print ("\nThe students final class grade is: ", student_grade_ave)
    
    # ***** Add student average to a final_grade list *****
    grade_ave.append(student_grade_ave)
    
    # ***** See if there are additional students *****
    another = input("\n\nIs there another student to enter? (y or n)").lower()

# ***** Display number of students in class *****
print ("\nThere were a total of", len(students), "students in the class.")

# ***** Display Alpha listing of student *****
print ("\nHere are their names in alphabetical order")
students.sort()
for m in students:
    print (m)
    
# ***** Calculate and display class average *****
class_average=0
for k in grade_ave:
    class_average+=k
print ("\nThe class average was: ", class_average/len(grade_ave))

# ***** Determine and print breakdown of grades given for class *****
a=0
b=0
c=0
d=0
f=0
for grd in grade_ave:
    if grd>=90:
        a=+1
    elif grd>=80:
        b+=1
    elif grd>=70:
        c+=1
    elif grd>=60:
        d+=1
    else:
        f+=1

print ("This is the class grade breakdown:")
print (a, "A's")
print (b, "B's")
print (c, "C's")
print (d, "D's")
print (f, "F's")


input("\n\nThank you for finishing the grades! Press Enter to Exit...")
    
