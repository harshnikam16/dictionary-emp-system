# Solution
employees = []

def add_employee():
    emp_id = "E" + str(101 + len(employees))
    name = input("Name: ")
    age = int(input("Age: "))
    dept = input("Dept: ")
    employees.append({"id": emp_id, "name": name, "age": age, "department": dept})
    print("Employee added.")

def remove_employee():
    emp_id = input("ID to remove: ")
    for emp in employees:
        if emp["id"] == emp_id:
            employees.remove(emp)
            print("Employee removed.")
            return
    print("Not found.")

def update_employee():
    emp_id = input("ID to update: ")
    for emp in employees:
        if emp["id"] == emp_id:
            name = input("Name (leave blank to keep current): ")
            age = input("Age (leave blank to keep current): ")
            dept = input("Dept (leave blank to keep current): ")
            if name:
                emp["name"] = name
            if age:
                emp["age"] = int(age)
            if dept:
                emp["department"] = dept
            print("Employee updated.")
            return
    print("Not found.")

def search_employee():
    search = input("ID or Name: ")
    found = [emp for emp in employees if search in emp["id"] or search.lower() in emp["name"].lower()]
    print(found if found else "Not found.")

def sort_employees():
    sort_by = input("Sort by (name/age/department): ")
    employees.sort(key=lambda x: x[sort_by])
    print(employees)

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
