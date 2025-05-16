# kai reikia grupuoti kintamuosius (kaupti kazkoki tai sarasa), each person has number, age, and citu
person1_name = "john"
person1_age = 36
person1_country = "Norway"

person2_name = "maria"
person2_age = 


#kai yra lauztiniai skliaustai tai ir  yra objektas . Dictionary (in Python), duomenu kaupimo vieta, 
personal_information_object = {
    "name": "john",
    "age": 36,
    "country": "Norway"
}
personal_information_object

#listss are used to store different varibales
my_list = [1,2,3,4,5]

my_list.append(6)

#CRUD (Create, Read, Update, Delete)
my_list.remove(6)
# accesing elemnts in the list
print("first elemin in the list is ", my_list[0])

#collections can have object inside - collection of opbjects. tai yra list of dictionary
people = [
    {
        "name": "john",
        "age": 36,
        "country": "Norway"
    },
    {   "name": "jan",
        "age": 16,
        "country": "Norway"
    }
]