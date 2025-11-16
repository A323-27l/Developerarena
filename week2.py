def score_li():
    stu_score= []


    while True:
        name = str(input("Enter student name: "))
        if name == "quit":
            break


        marks= int(input("Enter students marks : "))
        students = {'name': name, 'marks': marks}
        stu_score.append(students)
        print(stu_score)

        if 91 <= marks <= 100:
            print("You are Outstanding")

        elif 80 <= marks <= 90:
            print("You exceeded expectations")

        elif 71 <= marks <= 80:
            print("This is Acceptable")

        elif 0 <= marks <= 70:
            print("Fail")

score_li()
