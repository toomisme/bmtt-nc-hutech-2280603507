def truy_cap_phan_tu(tuple_data):
    first_element = tuple_data[0]
    last_element = tuple_data[-1]
    return first_element, last_element
#nhập tuple từ người dùng
input_tuple = eval(input("Nhập vào một tuple (vd: (1, 2, 3)): "))
first, last = truy_cap_phan_tu(input_tuple)
#in ra kết quả
print("Phần tử đầu tiên trong tuple là:", first)
print("Phần tử cuối cùng trong tuple là:", last)