class EmployeeTable:
    def __init__(self, data):
        self.data = data

    def display_table(self):
        print("Employee Table:")
        for row in self.data:
            print(row)

    def sort_table(self, sort_parameter):
        if sort_parameter == 1:  # Sort by Age
            self.data.sort(key=lambda x: x[2])
        elif sort_parameter == 2:  # Sort by Name
            self.data.sort(key=lambda x: x[1])
        elif sort_parameter == 3:  # Sort by Salary
            self.data.sort(key=lambda x: x[3])
        else:
            print("Invalid sorting parameter. Please choose 1, 2, or 3.")

# Example usage:
employee_data = [
    ['161E90', 'Ramu', 35, 59000],
    ['171E22', 'Tejas', 30, 82100],
    ['171G55', 'Abhi', 25, 100000],
    ['152K46', 'Jaya', 32, 85000]
]

employee_table = EmployeeTable(employee_data)

print("Original Employee Table:")
employee_table.display_table()

sorting_parameter = int(input("Enter sorting parameter (1. Age, 2. Name, 3. Salary): "))
employee_table.sort_table(sorting_parameter)

print("\nSorted Employee Table:")
employee_table.display_table()
