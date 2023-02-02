import controller


def set_new_contact(elements):
    print(elements)
    name = elements['name'].get()
    surname = elements['surname'].get()
    phone_number = elements['phone number'].get()
    contact = f'{name} {surname}: {phone_number}'
    elements['contacts list'].insert()