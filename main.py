from quiz import take_quiz, calculate_score
from leaderboard import save_result, view_leaderboard


while True:
    print("Welcome to the Quiz System")
    print("1. Take Quiz")
    print("2. View Leaderboard")
    print("3. Admin Mode")
    print("4. Exit")
    choice=input("Enter your choice: ")

    if choice=="1":
        score,incorrect_questions=take_quiz()
        name=input("Enter your name: ")
        save_result(name,score)
        calculate_score(score,len(incorrect_questions),incorrect_questions,0)
    elif choice=="2":
        view_leaderboard()
    elif choice=="3":
        admin_code=input("Enter admin code: ")
        if admin_code=="1234":
            admin_menu()
        else:
            print("Wrong admin code.")
    elif choice=="4":
        print("Goodbye")
        break
    else:
        print("Invalid choice. Try again.")
