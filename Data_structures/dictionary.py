#dictionary
x = {'name': 'Amoda', 'age': 23, 'city': 'Ampara'}
x["status"] = "single"
print(x)  # {'name': 'Amoda', 'age': 23, 'city': 'Ampara', 'status': 'single'}
print(x.keys())  # dict_keys(['name', 'age', 'city', 'status'])
print(x.values())  # dict_values(['Amoda', 23, 'Ampara', 'single'])


a = {1: 'Amoda', 2: 'Ampara', 3: 'Sri Lanka'}
print(a[1])  # Amoda
b = x.get(5, 'not found') #using this get method we can get the value of key otherwise we can set a default value
print(b)  # not found

#removing elements from dictionary
del x['age']  # removing age from dictionary
print(x)  # {'name': 'Amoda', 'city': 'Ampara', 'status': 'single'}
x.clear()  # removing all elements from dictionary

x = {
    "a": ["hello", "hi"],
    "b": ["world", "everyone"],


}

y = x["a"]
print(y)  # ['hello', 'hi']
y.append("good morning") #this is not valid for basic data types only valid for list
print(x)  # {'a': ['hello', 'hi', 'good morning'], 'b': ['world', 'everyone']}          
print(y)