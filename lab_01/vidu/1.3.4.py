#khai báo dictionary
my_dict ={}
person = {"name" : "Alice","age": 25, "city": "New York"}

#truy cập vào giá trị trong dict
print(person["name"])
print(person["age"])

#thêm hoặc cập nhật giá trị
person["email"] = "alice@example.com"
person["age"] = 26

#xoá
del person["city"]
age = person.pop("age")
