
person_list = []

while True: #tai yra nesibaigiantis loopas (while yra loop)
    person_name = input("Enter name")
    person_age = input("Enter age")
    person_country = input("Enter country")

    person = {
    "name": person_name,
    "age": person_age,
    "country": person_country
}

    person_list.append(person)

    for p in person_list: #p tiesiog kintamasis, o jo viduje yra objekats, 
    print(f"NAME: {p['name']}") 
