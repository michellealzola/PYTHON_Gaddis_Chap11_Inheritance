import employee


def get_employee_info(production_worker):
    if isinstance(production_worker, employee.ProductionWorker):
        print('The employee information: ')
        print('============================')
        print(f'Name: {production_worker.get_emp_name()}')
        print(f'Employee Number: {production_worker.get_emp_number()}')
        print(f'Shift Number: {production_worker.get_shift_num()}')
        print(f'Hourly pay rate: {production_worker.get_hourly_pay_rate()}')
    else:
        print('Not a worker')


def main():
    emp_name = input('Enter employee name: ')
    emp_num = input('Enter employee number: ')
    shift_num = int(input('Enter shift number (1 - day or 2 - night): '))
    hourly_rate = float(input('Enter hourly rate: '))

    production_worker = employee.ProductionWorker(emp_name, emp_num, shift_num, hourly_rate)

    get_employee_info(production_worker)


if __name__ == '__main__':
    main()
