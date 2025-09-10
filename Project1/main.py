# project
marks = []
while True:
    print("\n ----Student Marks Manager-----")
    print("1. ADD MARKS")
    print("2. VIEW ALL MARKS")
    print("3. EXIT")

    choice = int(input("ENTER YOUR CHOICE(1-3)"))
    if choice == 1:
        m = int(input("Enter Marks to add:"))
        marks.append(m)
        print("MARKS ADD SUCCESSFULLY!---")
    elif choice ==2:
        if marks:
            print("MARKS ARE:", marks)
        else:
            print("NO MARKS AVAILABLE!")
    elif choice == 3:
        print("PROGRAM ENDED-- GOOD BYE--")
        break