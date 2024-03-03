# main.py
from authentication import sign_in
from hrm import Employee

def main():
    # User authentication
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if sign_in(username, password):
        print("Authentication successful!\n")

        # Sample Employee instances
        employee1 = Employee("E001", "Mr. Kiten", "Chairman", "All", "xxxxxxxxxxxxx", "2020.01.01", ["2020.03.02", "2020.05.03", "2020.05.04"])
        employee2 = Employee("E002", "Mr. K. Josaph", "Head of the Finance Department", "Finance Department", "xxxxxxxxxxxxx", "2021.01.01", ["2021.03.05", "2023.02.02", "2021.10.20"])
        employee3 = Employee("E003", "Mr. John", "Software Developer", "Department of Development", "xxxxxxxxxxxxx", "2019.01.01", ["2019.06.05", "2019.02.03", "2019.03.01"])

        # Main menu options
        while True:
            print("Main Menu:")
            print("1. View Personal Information")
            print("2. Update Personal Information")
            print("3. Submit Leave Requests")
            print("4. View Company Policies")
            print("5. Access Work Schedules")
            print("6. Logout")

            choice = input("Enter your choice (1-6): ")

            if choice == "1":
                employee1.view_personal_information()  # You can choose the relevant employee based on the logged-in user
            elif choice == "2":
                # Update personal information for the logged-in employee
                new_contact_info = input("Enter new contact information: ")
                new_position = input("Enter new position: ")
                new_department = input("Enter new department: ")
                employee1.update_personal_information(new_contact_info, new_position, new_department)
            elif choice == "3":
                # Submit leave request for the logged-in employee
                leave_type = input("Enter leave type: ")
                duration = input("Enter duration: ")
                details = input("Enter details: ")
                employee1.submit_leave_request(leave_type, duration, details)
            elif choice == "4":
                employee1.view_company_policies()
            elif choice == "5":
                employee1.access_work_schedules()
            elif choice == "6":
                print("Logged out. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")

    else:
        print("Authentication failed. Exiting...")

if __name__ == "__main__":
    main()
