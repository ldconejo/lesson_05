from sys import exit
import csv

def load_from_csv():
    try:
        with open("user_database.csv", "r") as database_file:
            column_names = ("user_name", "user_last_name", "user_email")
            all_rows = csv.DictReader(database_file, fieldnames=column_names)
            for row in all_rows:
                list_of_rows.append(row)
        print("INFO: All rows loaded from database file!")
    except FileNotFoundError:
        print("ERROR: Database file not found!")

def save_to_csv():
    column_names = ("user_name", "user_last_name", "user_email")
    with open("user_database.csv", "w") as database_file:
        writer = csv.DictWriter(database_file, fieldnames=column_names)
        writer.writerows(list_of_rows)
    print("INFO: All rows saved to database!")

def add_user():
    user_name = input("Enter the user's name: ")
    user_last_name = input("Enter the user's last name: ")
    user_email = input("Enter the user's email: ")
    new_row = {
        "user_name": user_name,
        "user_last_name": user_last_name,
        "user_email": user_email
    }
    list_of_rows.append(new_row)
    print("INFO: New user added!")

def delete_user():
    user_email = input("Enter the email from the user you want to delete: ")
    for row in list_of_rows:
        if row["user_email"] == user_email:
            list_of_rows.remove(row)
            print("INFO: User has been removed!")
            return
    print("ERROR: User not found!")

def print_table():
    print("Name \t\tLast Name \te-mail")
    for row in list_of_rows:
        print(f"{row["user_name"]} \t\t{row["user_last_name"]} \t\t{row["user_email"]}")

def quit_program():
    exit()

if __name__ == "__main__":
    list_of_rows = []
    main_menu = """
        1. Load csv file.
        2. Save to csv file.
        3. Add user.
        4. Delete user.
        5. Print table.
        6. Quit.
    """

    while True:
        print(main_menu)
        user_choice = input("Please select an option: ")

        match user_choice:
            case "1":
                load_from_csv()
            case "2":
                save_to_csv()
            case "3":
                add_user()
            case "4":
                delete_user()
            case "5":
                print_table()
            case "6":
                quit_program()
            case _:
                print("ERROR: Please select a valid option")