# hrm.py

class Employee:
    def __init__(self, emp_id, name, position, department, contact_info, hire_date, leave_details):
        self.emp_id = emp_id
        self.name = name
        self.position = position
        self.department = department
        self.contact_info = contact_info
        self.hire_date = hire_date
        self.leave_details = leave_details

    def view_personal_information(self):
        print("Employee ID:", self.emp_id)
        print("Employee Name:", self.name)
        print("Designation:", self.position)
        print("Department:", self.department)
        print("Contact Information:", self.contact_info)
        print("Appointment Date:", self.hire_date)
        print("Leave Details:", ", ".join(self.leave_details))
        print()

    def update_personal_information(self, new_contact_info, new_position, new_department):
        self.contact_info = new_contact_info
        self.position = new_position
        self.department = new_department
        print("Personal information updated successfully.")
        print()

    def submit_leave_request(self, leave_type, duration, details):
        leave_request = f"{duration}: {leave_type} - {details}"
        self.leave_details.append(leave_request)
        print("Leave request submitted successfully.")
        print()

    def view_company_policies(self):
        print("Company Policies:")
        print("1. Dress Code: Business casual attire is required.")
        print("2. Working Hours: 9:00 AM to 5:00 PM, Monday to Friday.")
        print("3. Code of Conduct: Follow ethical practices and treat colleagues with respect.")
        print()

    def access_work_schedules(self):
        print("Work Schedule:")
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Position:", self.position)
        print("Department:", self.department)
        print("Work Hours: 9:00 AM to 5:00 PM")
        print("Upcoming Events: Team Meeting on 2024-03-10, Training Session on 2024-03-15")
        print()
