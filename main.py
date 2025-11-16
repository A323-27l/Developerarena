def person_info():
    name = str(input("Enter name : ")).upper().strip()
    age =  int(input("Enter age :"))
    city= str(input("Enter city name :")).upper().strip()
    hobbies = input("Enter Hobby (comma separate) :").upper().split(" ")
    hobbies =  [hobby.strip() for hobby in hobbies]

    print("=" *10 + "PERSONAL INFORMATION DETAILS" + "=" * 10)
    print(" " *10 + "Name :",  name)
    print(" " *10 + "Age :",  age)
    print(" " *10 + "City :", city)
    print(" " *10 + "Hobbies :",  hobbies)
    print("*" * 20 + "END" + "*" * 20)

person_info()