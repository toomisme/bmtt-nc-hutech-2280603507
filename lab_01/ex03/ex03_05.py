def dem_so_lan_xuat_hien(lst):
    count_dict = {}
    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict
#nhập danh sách từ người dùng
input_list= input("Nhập vào danh sách, cách nhau bởi dấu cách: ")
words_list = input_list.split()
#sử dụng hàm và in ra kết quả
so_lan_xuat_hien = dem_so_lan_xuat_hien(words_list)
print("Số lần xuất hiện của từng phần tử trong danh sách là:", so_lan_xuat_hien)
