# Solution
employees = {
    "E101": {"name": "Alice Johnson", "age": 30, "department": "HR"},
    "E102": {"name": "Bob Smith", "age": 25, "department": "IT"}
}

def add_employee():
    emp_id = "E" + str(101 + len(employees))
    name = input("Name: ")
    age = int(input("Age: "))
    dept = input("Dept: ")
    employees[emp_id] = {"name": name, "age": age, "department": dept}
    print("Employee added.")

def remove_employee():
    emp_id = input("ID to remove: ")
    if emp_id in employees:
        del employees[emp_id]
        print("Employee removed.")
    else:
        print("Not found.")

def update_employee():
    emp_id = input("ID to update: ")
    if emp_id in employees:
        name = input("Name (leave blank to keep current): ")
        age = input("Age (leave blank to keep current): ")
        dept = input("Dept (leave blank to keep current): ")
        if name:
            employees[emp_id]["name"] = name
        if age:
            employees[emp_id]["age"] = int(age)
        if dept:
            employees[emp_id]["department"] = dept
        print("Employee updated.")
    else:
        print("Not found.")

def search_employee():
    search = input("ID or Name: ")
    found = {}
    for k, v in employees.items():
        if search in k or search.lower() in v["name"].lower():
            found[k] = v
    print(found if found else "Not found.")

def sort_employees():
    sort_by = input("Sort by (name/age/department): ")
    sorted_employees = dict(sorted(employees.items(), key=lambda x: x[1][sort_by]))
    print(sorted_employees)

def main():
    while True:
        choice = input("\n1.Add 2.Remove 3.Update 4.Search 5.Sort 6.Exit: ")
        if choice == "1":
            add_employee()
        elif choice == "2":
            remove_employee()
        elif choice == "3":
            update_employee()
        elif choice == "4":
            search_employee()
        elif choice == "5":
            sort_employees()
        elif choice == "6":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
