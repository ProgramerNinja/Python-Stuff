
#Jared McMahon
#12/18
#avg grades



gradelist =[]

def getGrade(gradelist):

    while True:
        maxGrade = 100
        grade = input("enter in a grade, to exit press space bar")
        if grade == " ":
            break
        elif grade.isdigit() == True:
            grade = float(grade)
            if grade <= maxGrade:
                gradelist.append(grade)
            else:
                q=input("Are you sure this is" + str(grade) + "is a good grade y or n")
                if q == "y":
                    gradelist.append(grade)
                else:
                    print("that's not valid")
        else:
            print("that's not valid")

def avgfunction(gradelist):
    total = sum(gradelist)
    for grade in gradelist:
        total += grade
    avg = total / len(gradelist)
    return avg

def main(gradelist):

    getGrade(gradelist)
    avg = avgfunction(gradelist)
    print("your grade is ",avg)
    xmax = max(gradelist)
    xmin = min(gradelist)
    print(xmax)
    print(xmin)

main(gradelist)
