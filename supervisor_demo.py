import employee


def get_employee_info(shift_supervisor):
    if isinstance(shift_supervisor, employee.ShiftSupervisor):
        print('The employee information: ')
        print('============================')
        print(f'Name: {shift_supervisor.get_emp_name()}')
        print(f'Employee Number: {shift_supervisor.get_emp_number()}')
        print(f'Annual Salary: {shift_supervisor.get_annual_salary():,.2f}')
        print(f'Annual Bonus: {shift_supervisor.get_annual_bonus():,.2f}')
    else:
        print('Not a worker')


def main():
    emp_name = input('Enter employee name: ')
    emp_num = input('Enter employee number: ')

    annual_sal = float(input('Enter annual salary: '))
    annual_bonus = float(input('Enter annual bonus: '))

    shift_supervisor = employee.ShiftSupervisor(emp_name, emp_num, annual_sal, annual_bonus)

    get_employee_info(shift_supervisor)


if __name__ == '__main__':
    main()
