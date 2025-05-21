def dao_nguoc_list(list):
    return list[::-1]
#nhập danh sách số nguyên từ người dùng và xử lý chuỗi
input_list= input("Nhập vào danh sách số nguyên, cách nhau bởi dấu phẩy: ")
numbers = list(map(int, input_list.split(",")))
#sử dụng hàm và in ra kết quả
list_dao_nguoc = dao_nguoc_list(numbers)
print("Danh sách đảo ngược là:", list_dao_nguoc)