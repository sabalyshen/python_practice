from employee import Employee


employee_payment = Employee()
print("Enter 'q' at any time to quit. ")

while True:
    last_name = input("Please enter your last name:")
    if last_name == 'q':
        break
    first_name = input("Please enter your first name:")
    if first_name == 'q':
        break
    salary = input("Enter salary:")
    if salary == 'q':
        break
    employee_payment.neat_name(last_name, first_name)
    employee_payment.employee_payment(salary)
    employee_payment.name_salary()

print("Which person you want raise his(her) salary? ")
while True:
    last_name = input("Please enter last name:")
    if last_name == 'q':
        break
    first_name = input("Please enter first name:")
    if first_name == 'q':
        break

    name = last_name + ' ' + first_name
    employee_payment.give_raise(name.title())
