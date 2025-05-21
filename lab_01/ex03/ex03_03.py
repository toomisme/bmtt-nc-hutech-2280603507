def tao_tuple_tu_list(lst):
    return tuple(lst)
#nhập danh sách số nguyên từ người dùng và xử lý chuỗi
input_list= input("Nhập vào danh sách số nguyên, cách nhau bởi dấu phẩy: ")
numbers = list(map(int, input_list.split(",")))
my_tuple = tao_tuple_tu_list(numbers)
print("List: ", numbers)
print("Tuple từ list: ", my_tuple)