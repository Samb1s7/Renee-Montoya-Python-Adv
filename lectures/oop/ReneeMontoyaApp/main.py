from lectures.oop.ReneeMontoyaApp.models.plant import Plant
from lectures.oop.ReneeMontoyaApp.models.employee import Employee
from lectures.oop.ReneeMontoyaApp.framework.models import Model


class Menu:

    # 1. Add new Plant
    # 2. Add new Employee
    # 3. Get plant by id
    # 4. Get employee by id

    def add_new_plant(self):
        id = int(input("ID: "))
        location = input("Location: ")
        name = input("Name: ")
        director_email = int(input("Director e-mail: "))
        director_id = Model.get_by_email(director_email)
        plant = Plant(id, location, name, director_id)
        plant.save()

    def add_new_employee(self):
        id = int(input("ID: "))
        name = input("Name: ")
        email = input("Email: ")
        department_type = input("Department Type: ")
        department_id = int(input("Department id: "))
        employee = Employee(id, name, email, department_type, department_id)
        employee.save()

    def get_plant(self):
        id = int(input("ID: "))
        plant = Plant.get_by_id(id)
        print(plant)

    def get_employee(self):
        id = int(input("ID: "))
        employee = Employee.get_by_id(id)
        print(employee)

    def get_employee_email(self):
        email = int(input("ID: "))
        employee = Employee.get_by_id(id)
        print(employee)


menu = Menu()

if __name__ == '__main__':
    while True:
        print(
            "Choose a menu item by number: \n" +
            "1. Add new Plant \n" +
            "2. Add new Employee \n" +
            "3. Get plant by id \n" +
            "4. Get employee by id \n"
        )
        menu_flag = int(input("Your choose: "))
        if menu_flag == 1:
            menu.add_new_plant()
        elif menu_flag == 2:
            menu.add_new_employee()
        elif menu_flag == 3:
            menu.get_plant()
        elif menu_flag == 4:
            menu.get_employee()