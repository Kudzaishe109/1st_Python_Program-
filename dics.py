#Dictionaries
# student = {
#     "name" : "Kudzi",
#     "age" : 21,
#     "gender" : "male"
# }
 
# student["name"] = "Decent"
# print(student)

# Country = {
#     'name' : "Zimbabwe",
#     'provincies' : 10,
#     'capital_city' : "Hre",
#     'population' : 10e6 
# }

# Country['capital_city'] = 'Mt Hampden'

# print(Country['capital_city'])
# Country.update({'language' : 'Shona', 'size' : 10e100})
# del (Country['population'])
# # print(Country)

# print(Country.pop(['language']))

capitals = {'USA' : 'DC',
            'Zim' : 'Harare',
            'SA' : 'Pretoria',
            'Nigeria' : 'Lagos'
            }

# capitals['Zim'] = 'Mt Hmpden'
# capitals.update({'Zim' : 'Hre', 'Botswana' : 'Gaborone'})
# print(capitals['Zim'])

# print(capitals.get('Zim'))
#print(capitals.__getitem__('Zim'))
# print(capitals.pop('Zim'))
capitals.popitem()
print(capitals)
