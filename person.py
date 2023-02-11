class Person:
    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_phone(self, phone):
        self.__phone = phone

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone


class Customer(Person):
    def __init__(self, name, address, phone, cust_number, mailing_list):
        Person.__init__(self, name, address, phone)
        self.__cust_number = cust_number
        self.__mailing_list = bool(mailing_list)

    def set_cust_number(self, cust_number):
        self.__cust_number = cust_number

    def set_mailing_list(self, mailing_list):
        self.__mailing_list = bool(mailing_list)

    def get_cust_number(self):
        return self.__cust_number

    def get_mailing_list(self):
        return self.__mailing_list
