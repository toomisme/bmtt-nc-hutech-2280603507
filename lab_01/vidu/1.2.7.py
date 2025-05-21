#khai báo chuỗi 
#sử dụng dấu ngoặc đơn
string_single_quotes = 'hi'

#sử dụng dấu ngoặc đơn
string_double_quotes = "hi"

#sử dụng dấu ngoặc đơn
string_triple_quotes = '''hi


'''

#truy cập lý tự trong chuỗi
my_string = "Hello, World!"
print(my_string[0])
print(my_string[7])

#các phép xử lý chỗi trong py
#cắt chuỗi
my_string = "Hello, World!"
print(my_string[7:])
print(my_string[:5])
print(my_string[3:8])

#ghép chuỗi
string1 = "Hello"
string2 = "World"
concatenated_string = string1 + " " + string2

#độ dài chuỗi
my_string = "Hello, World!"
length = len(my_string)

#một số hàm dùng để xử lý chuỗi trong py
my_string = "       Hello, World!            "
print(my_string.strip()) #loại bỏ khoảng trắng

my_string = "Hello, World!"
print(my_string.split(",")) #phân tách chuỗi

my_string = "Hello, World!"
print(my_string.replace("Hello", "Hi")) #thay thế chuỗi