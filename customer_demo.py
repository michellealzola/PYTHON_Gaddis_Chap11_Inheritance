import person


def main():
    name = 'Nancy'
    address = 'Happy Ave., SW'
    phone = '1234567890'
    cust_num = '123456'
    mailing_list = True

    customer = person.Customer(name, address, phone, cust_num, mailing_list)

    if isinstance(customer, person.Customer):
        print(f'Name: {customer.get_name()}')
        print(f'Address: {customer.get_address()}')
        print(f'Phone: {customer.get_phone()}')
        print(f'Customer Number: {customer.get_cust_number()}')
        print(f'Wishes to be in the mailing list?: {customer.get_mailing_list()}')


if __name__ == '__main__':
    main()
