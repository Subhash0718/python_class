class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def calculate(self):
        total = sum(self.marks)
        return total
    
    def average(self):
        avg = sum(self.marks)/len(self.marks)
        return avg
    
    def grade_of(self):
        grade = ""
        percentage = sum(self.marks)/len(self.marks)
        
        if(percentage>=90):
            grade = "A"
        
        elif(percentage>=80):
            grade = "B"

        elif(percentage>=70):
            grade = "C"

        elif(percentage>=60):
            grade ="D"

        else:
            grade = "F"

        return grade
    


print("Welcome to the Student Grade Management System...........")
print("Please follow the below details")
students = []
while(True):
    print("1. Enter the Student Name and the marks\n2. See the details\n3. Exit the program")
    choice = int(input("Enter the choice "))
    match choice:
        case 1:
            name = (input("Enter the name: "))

            mark = []
            print("Enter either 3 subject marks or 5 subject marks")
            m = int(input("Enter the number of the subjects: "))
            if(m==3 or m==5):
                for i in range(0,m):
                    n = int(input("Enter your mark: "))
                    mark.append(n)

            s = Student(name,mark)
            students.append(s)
            print()
            print()


        case 2:
            if(len(students)!=0):
                for s in students:
                    print("Student Report".center(22,"~"))
                    print("----------------------------------------------------")
                    print("Student name: ",s.name)
                    print("Marks: ",s.marks)
                    print("Total Marks Scored: ",s.calculate())
                    print("Average: ",s.average())
                    print("Grade: ",s.grade_of() )
                    print("---------------------End of Report------------------------------")

            else:
                print("First fill the student details and then come here!!!!!")
            
            
            print()
            print()
            print()



        case 3:
            print("Exiting................")
            print()
            break

        case _ :
            print("Please Enter the valid Choice")
            print()
            print()

print("Thanks for using Student Grade Management System.........")
