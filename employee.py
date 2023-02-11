class Employee:
    def __init__(self, emp_name, emp_number):
        self.__emp_name = emp_name
        self.__emp_number = emp_number

    def set_emp_name(self, emp_name):
        self.__emp_name = emp_name

    def set_emp_number(self, emp_number):
        self.__emp_number = emp_number

    def get_emp_name(self):
        return self.__emp_name

    def get_emp_number(self):
        return self.__emp_number


class ProductionWorker(Employee):
    def __init__(self, emp_name, emp_number, shift_num, hourly_pay_rate):
        Employee.__init__(self, emp_name, emp_number)
        self.__shift_num = shift_num
        self.__hourly_pay_rate = hourly_pay_rate

    def set_shift_num(self, shift_num):
        if shift_num == 1 or shift_num == 2:
            self.__shift_num = shift_num
        else:
            print('Not a valid shift number')

    def set_hourly_pay_rate(self, hourly_pay_rate):
        self.__hourly_pay_rate = hourly_pay_rate

    def get_shift_num(self):
        return self.__shift_num

    def get_hourly_pay_rate(self):
        return self.__hourly_pay_rate


class ShiftSupervisor(Employee):
    def __init__(self, emp_name, emp_number, annual_salary, annual_bonus):
        Employee.__init__(self, emp_name, emp_number)
        self.__annual_salary = annual_salary
        self.__annual_bonus = annual_bonus

    def set_annual_salary(self, annual_salary):
        self.__annual_salary = annual_salary

    def set_annual_bonus(self, annual_bonus):
        self.__annual_bonus = annual_bonus

    def get_annual_salary(self):
        return self.__annual_salary

    def get_annual_bonus(self):
        return self.__annual_bonus



