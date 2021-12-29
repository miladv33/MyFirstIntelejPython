person = {
    'name': "milad",
    'age': 27
}
person2 = dict(name="miladi", age=15)
print(person2)
person2['city'] = 'tehran'
print(person2)

# delete
del person2['name']
person2.pop('age')
print(person2)

# clear
person2.clear()
print(person2)