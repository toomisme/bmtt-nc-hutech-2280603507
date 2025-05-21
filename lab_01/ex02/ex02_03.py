#nhập số từ người dùng
so = int(input("Nhập một số nguyên: "))
#kiểm tra số đó là số chẵn hay lẻ
if so % 2 == 0:
    print(so, "là số chẵn.")
else:
    print(so, "là số lẻ.")